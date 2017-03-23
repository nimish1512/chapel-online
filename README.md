# chapel-online
GSOC 17 project prototype for Chapel(Web development Idea)

Requirements:
1) Apache2 Server (not neeed for browser client)
    Command : sudo apt-get install apache2  and then sudo /etc/init.d/apache2 restart
2) Chapel Compiler (onot neeed for browser client)
    Refer here: http://chapel.cray.com/download.html  
3) Python 3 n above (not neeed for browser client)
    Command : sudo apt-get install python3
4) PHP 5 (not neeed for browser client)
    Command : sudo apt-get install php5 libapache2-mod-php5
Install:
1) clone the repository
2) change directory to chapel-online
3) Run setup file : "sudo bash setup.sh your_username"
4) open your favourite browser and type in the url field: "localhots:80/chapel-online/"

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

