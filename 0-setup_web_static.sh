#!/usr/bin/env bash
# 0. Prepare your web servers

sudo apt-get -y update >/dev/null 2>&1
sudo apt-get -y install nginx >/dev/null 2>&1

sudo mkdir -p /data/ >/dev/null 2>&1
sudo mkdir -p /data/web_static/ >/dev/null 2>&1
sudo mkdir -p /data/web_static/releases/ >/dev/null 2>&1
sudo mkdir -p /data/web_static/shared/ >/dev/null 2>&1
sudo mkdir -p /data/web_static/releases/test/ >/dev/null 2>&1

html_content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$html_content" | sudo tee /data/web_static/releases/test/index.html >/dev/null 2>&1

if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current >/dev/null 2>&1
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current >/dev/null 2>&1


content=\
"
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/;
        index index.html index.htm index.nginx-debian.html;
        server_name _;

        location /hbnb_static {
            alias /data/web_static/current/;
        }
}
"



sudo chown -R ubuntu:ubuntu /data/ >/dev/null 2>&1
echo "$content" | sudo tee /etc/nginx/sites-available/default >/dev/null 2>&1
sudo service nginx restart >/dev/null 2>&1
