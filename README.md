# WebhookListener (Moved to GitLab)
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

A python and flask application to receive and log webhooks. If they are webhooks from PoGo++ or iSpoofer, it will also decode them.

## Installation

### Requirements
Install the following:

* python3
* python3-pip
* git

Verify version using:
```
$ python3 --version
Python 3.6.7
$ pip3 --version
pip 9.0.1 from /home/pogo/python3-test/lib/python3.6/site-packages (python 3.6)
```

This also requires a webhook source, which is not provided. If the webhooks are from PoGo++ or iSpoofer, you can also use options to decode them.

### Downloading the Application

To run a copy from the latest develop branch in git you can clone the repository:
`git clone https://github.com/Kneckter/WebhookListener`

### Installing Modules

Open up your shell (cmd.exe/terminal.app) and change to the directory of WebhookListener.

Install the Python dependencies with the following command:

Windows:
`pip3 install -U -r requirements.txt`
Linux/OSX:
`sudo -H pip3 install -U -r requirements.txt`

### Basic Launching

Start the application with the following command:
`python3 runserver.py`

You can display the optional parameters by using the `--help` flag. No webhook data will be displayed unless at least one logging option is set. All options can be set on the command line or in the `./conf/config.ini` file. If you setup a `config.ini` file, the program will read the settings automatically without specifying it in the command line.

Once your setup is running, open your browser to http://localhost:5000/webhook and you should see text displaying `Listening for webhooks`. 

## Integration

If you are running an NGINX reverse proxy for your main webhook receiver, you can setup a mirror so you do not need to change your webhook generating application. Below is an example of how to setup the server block in NGINX.
```
server {
    listen 9002;
    server_name  127.0.0.1;

    location / {
        mirror /mirror;
        proxy_pass http://127.0.0.1:9001;
        access_log off;
        error_log /dev/null;
    }
    location /mirror {
        internal;
        proxy_pass http://127.0.0.1:5000/webhook;
        access_log off;
        error_log /dev/null;
    }
}
```
