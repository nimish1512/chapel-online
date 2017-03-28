from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory
import docker, json
import random, string
import os

class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Connecting...")  

    def onOpen(self):
        try:
            client = docker.from_env()
            self.cli = client
            self.file_locate = {'/home/nemo1521/twisted-gsoc/final/files/':{'bind':'/mnt/source/','mode':'rw'}}
            self.cont = self.cli.containers.create(image="buildpack-deps:latest",detach=False,mem_limit=2147483648,memswap_limit=2147483648,tty=True,volumes=self.file_locate,working_dir='/mnt/source')
            self.file_name= ''.join(random.choice(string.lowercase) for i in range(5))	
        except Exception:
            print("Failed"+str(Exception))    

    def onMessage(self, payload,isBinary=False):
    	try:
    		data = payload.decode('utf8')
    		print(str(data))
    		if data=="pause,!!" and self.cont.status=="created" or self.cont.status=="running":
    			print(self.cont.status)
    			self.cont.pause()
    			print("Paused")
    			rep = "Program Paused"
    			rep = rep.encode('utf8')
    			self.sendMessage(rep)

    		elif data=="resume,!!" or self.cont.status=="paused":
    			print(self.cont.status)
    			self.cont.unpause()
    			print("Resumed")
    			rep = "Program Resumed"
    			rep = rep.encode('utf8')
    			self.sendMessage(rep)

    		else:	
    			f = open('/home/nemo1521/twisted-gsoc/final/files/'+self.file_name+'.c','w+')
    			f.write(data)
    			f.close()
    			print("file created")
    			self.cont.start()
    			ans = self.cont.exec_run(cmd="gcc -o "+self.file_name+" "+self.file_name+".c",stdout=True,stderr=True,stdin=False,tty=False,privileged=False,user='root',detach=False,stream=True)
    			if ans:
    				print("In here")
    				ans  = self.cont.exec_run(cmd="./"+self.file_name,stdout=True,stderr=True,stdin=False,tty=False,privileged=False,user='root',detach=False,stream=True)
    			for lines in ans:
    				print(lines.strip())
    				en_line = lines.encode('utf8')
    				self.sendMessage(en_line)

        except Exception:
        	print("Doesn't work")	

    def onClose(self, wasClean, code, reason):
        try:
            self.cont.stop()
            self.cont.remove(force=True)
        except Exception:
            print(str(Exception))    

if __name__ == '__main__':

    import sys
    from twisted.python import log
    from twisted.internet import reactor

    #log.startLogging(sys.stdout)

    factory = WebSocketServerFactory(u"ws://127.0.0.1:8000")
    factory.protocol = MyServerProtocol
    # factory.setProtocolOptions(maxConnections=2)

    # note to self: if using putChild, the child must be bytes...

    reactor.listenTCP(8000, factory)
    reactor.run()
