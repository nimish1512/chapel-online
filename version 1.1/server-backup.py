from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory
from twisted.internet import protocol    
import random, string
import os
import subprocess 

class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        try:
            print("Connecting...")
        except Exception:
            print("Failed"+str(Exception))    

    def onOpen(self):
        try:
            self.cont_name = ''.join(random.choice(string.lowercase) for i in range(5)) 
            self.file_name = self.cont_name
            cmd = "docker create --name "+self.cont_name+" -it buildpack-deps:latest"
            a = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            self.contid = str(a.stdout.read())
            self.cont = str(self.contid[:12])
            self.cont_status = "created"
        except Exception:
            print("Couldn't create container")
        
    def onMessage(self, payload,isBinary=False):
            data = payload.decode('utf8')
            print(str(data))
            print(self.cont_status)
            if data=="pause,!!" and self.cont_status=="running":
                cmd = "docker pause "+self.cont_name
                a = subprocess.Popen([cmd], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                response = str(a.stderr.read())
                print(response)
                self.cont_status = "paused"
                reply = "Program Paused"
                reply = reply.encode('utf8')
            
            elif data=="resume,!!" and self.cont_status=="paused":
                cmd = "docker unpause "+self.cont_name
                a = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                response = str(a.stdout.read())
                self.cont_status="running"

            else:    
                f = open('/tmp/user_files/'+self.file_name+'.c','w+')
                f.write(data)
                f.close()
                cmd = "gcc /tmp/user_files/"+self.file_name+".c -o /tmp/user_files/"+self.file_name
                a = subprocess.call(cmd, shell=True)
                errors = str(a)
                if errors == "0":
                    print("file created")
                    cmd = "docker start "+self.cont_name
                    a = str(subprocess.call(cmd, shell=True))
                    if a=="0":
                        self.cont_status="running"
                        cmd = "docker cp /tmp/user_files/"+self.file_name+" "+self.cont_name+":/tmp/"+self.file_name
                        a = subprocess.call(cmd, shell=True)
                        if str(a) == "0":
                            cmd = "docker exec "+self.cont_name+" /tmp/./"+self.file_name
                            self.popen_in_thread(lambda line: reactor.callFromThread(lambda: self.sendMessage(line.encode("utf-8"))),[cmd], shell=True, stdout=subprocess.PIPE, bufsize=1) 
                        else:
                            reply = "Couldn't copy file"
                            reply = reply.encode('utf8')
                            self.sendMessage(reply)
                    else:
                        reply = "Couldn't start container"
                        reply = reply.encode('utf8')
                        self.sendMessage(reply)                
                else:
                    errors = "There are errors in your code.\nNote that this doesn't support Chapel code yet.\nPlease give a valid C code "
                    errors = errors.encode('utf8')
                    self.sendMessage(errors)                   
            end = "00,0"
            self.sendMessage(end.encode('utf8'))     
    
    def popen_in_thread(self,callback, *args, **kwargs):
        def threaded():
            a = subprocess.Popen(*args, **kwargs)
            for line in iter(a.stdout.readline, b''):
                callback(line)
        reactor.callInThread(threaded)
    
    def onClose(self, wasClean, code, reason):
        try:
            cmd = "docker stop "+self.cont_name
            a = subprocess.call(cmd, shell=True)
            cmd = "docker rm -f "+self.cont_name
            a = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE)
            if str(a.stdout.read()) == self.cont_name:
                print("Closed container...")
        except Exception:
            print(str(Exception))    

if __name__ == '__main__':

    import sys
    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)
    #reactor.run()

    factory = WebSocketServerFactory(u"ws://139.59.11.10:8000")
    factory.protocol = MyServerProtocol
    # factory.setProtocolOptions(maxConnections=2)

    # note to self: if using putChild, the child must be bytes...

    reactor.listenTCP(8000, factory)
    reactor.run()
