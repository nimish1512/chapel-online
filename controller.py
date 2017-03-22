import sys
import os
from subprocess import Popen, PIPE
filename = sys.argv[1]
#Generation of filename for executable
executable = filename+"_exec"
change_owner = 'sudo bash sch.sh '+filename
'''
To change the ownership of the .chpl file from www-data to current_user

When index.php generates the .chpl file, it is owned by 
the 'www-data' user of Apache since the PHP processes running
is in Apache's domain. Therefore, no execution rights are given to 
the .chpl file for users other than 'www-data'. To fix this, 'sch.sh' 
changes the ownership of .chpl file to your user acc.
'''
os.system(change_owner)
'''
The standard 'chpl -o executable_name filename' command
for compiling a chapel program. In this case, relative 
path to the 'chpl' binary has been given. You can run 
the same by giving only 'chpl' if CHPL_HOME environment
variable is set on your system. Usually, chapel binary is found in
chapel/bin/linux64/
'''
error = Popen(['chpl','-o',executable,filename],stdout=PIPE,stderr=PIPE)
op = error.communicate()
'''
Checking for compilation errors
'''
if op[1]:
	print(str(op[1])+str("//error"))
'''
If no errors found, run the executable and capture the output
of the program. Send this output to the calling PHP file.
'''
else:
	run = './'+executable
	execute = Popen([run], stdin=PIPE, stdout=PIPE)
	out = repr(execute.stdout.read())
	print(str(out))		 
