#!/usr/bin/env bash
# Setup Web servers for the static files

# Install nginx if it isn't installed already
sudo apt-get update
sudo apt-get -y install nginx

# Create directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir /data/web_static/shared

# Change owner of the data directory
sudo chown -R ubuntu:ubuntu /data/

# Create test html file
echo "<!DOCTYPE html><html><body>Hello</body></html>" > /data/web_static/releases/test/index.html

# Create link from test to current
ln -fs -T /data/web_static/releases/test /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

config="
server {
	   listen 80 default_server;
	   listen [::]:80 default_server;

	   root /var/www/html;

	   index index.html index.htm index.nginx-debian.html;

	   server_name _;

	   location /hbnb_static {
	   			alias /data/web_static/current/;
	   }

	   location / {
	   			try_files \$uri \$uri/ =404;
	   }
}
"

echo "${config}" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
