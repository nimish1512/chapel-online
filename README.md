# chapel-online
GSOC 17 project prototype for Chapel(Web development Idea)

Requirements:
1) Apache2 Server (not neeed for browser client)
2) Chapel Compiler (onot neeed for browser client)
3) Python 3 n above (not neeed for browser client)

Note:
1) You will need to edit your visudo file to provide passwordless root access to the files. To do so:
  1) open a Terminal and type sudo visudo
  2) put in your password
  3) type the following command below this line : (%sudo   ALL=(ALL:ALL) ALL)
      Type this: your_username ALL= NOPASSWD: /absolute/path/to/sch.sh
  4) Save and exit
  5) Replace your_username with "Your username" in sch.sh Haha!!
  
Working Features:
1) Full Restful API
2) Dynamic File and executable generation
3) Permission Management for files
4) Basic UI
5) Compilation Error handling
6) Temporary file management

Work in Progress:
1) Full fledge code editor with code highlighting support for Chapel
2) Support for run-time input to programs
3) Better file organisation at Backend
4) Logs geneation and Performance analysis

