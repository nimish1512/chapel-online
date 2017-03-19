import sys
import pwd
import os
filename = sys.argv[1]
executable = filename+"_exec"
command = '/home/nemo1521/chapel/chapel-1.14.0/bin/linux64/chpl -o '+executable+' '+filename
uid = pwd.getpwnam("nemo1521").pw_uid
change_owner = 'sudo bash sch.sh '+filename
os.system(change_owner)
os.system(command)
run = './'+executable
out = os.popen(run).readlines()
print(out)