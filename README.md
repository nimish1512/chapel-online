# Chapel-Online

GSOC 17 project prototype for Chapel(Web development Idea)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Things that you'll need :
```
python 2.7.9
Autobahn
Twisted 17.9.0
Download and build chapel : http://chapel.cray.com/download.html
Apache Server
Docker
```

### Installing

Steps to setup your working environment
```
sudo apt-get install apache2
pip install autobahn[twisted]
pip install docker
pip install twisted
```
```

```
Providing necessary permissions (please take a backup of /etc/sudoers file before doing this)

Copying client to www folder
```
sudo mkdir /var/www/chapel-online
sudo mv  -v path/to/cloned-directory/client/* /var/www/chapel-online/
```
## Running the tests
Open up your favourite browser and type the following in url bar
```
localhost:80/chapel-online/
```
Demo
```
Landing Page
```
![Landing_page](https://github.com/nimish1512/chapel-online/blob/master/landing_page.png)
```
Compiling Page
```
![Compiling_page](compiling.png)
```
Result Page
```
![Output_page](output_page.png)

## Deployment

Additional notes about how to deploy this on a live system

## Built With

* [Bootstrap](http://getbootstrap.com/getting-started/) - Frontend framework 
* [Twisted Engine](https://twistedmatrix.com/) - Async Server Engine
* [Python 2.7](https://python.org) - Main controllers

## Authors

* **Nimish Ronghe** - *Initial work* - [Tensorflow](https://github.com/nimish1512)

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
