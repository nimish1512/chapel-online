import sys
import pwd
import os
from subprocess import Popen, PIPE
filename = sys.argv[1]
executable = filename+"_exec"
command = '/home/nemo1521/chapel/chapel-1.14.0/bin/linux64/chpl -o '+executable+' '+filename
uid = pwd.getpwnam("nemo1521").pw_uid
change_owner = 'sudo bash sch.sh '+filename
os.system(change_owner)
error = Popen(['/home/nemo1521/chapel/chapel-1.14.0/bin/linux64/chpl','-o',executable,filename],stdout=PIPE,stderr=PIPE)
op = error.communicate()
if op[1]:
	print(op[1])
else:
	run = './'+executable
	execute = Popen([run], stdin=PIPE, stdout=PIPE)
	out = repr(execute.stdout.readline())
	print(str(out))		 
