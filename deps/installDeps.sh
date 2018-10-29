#!/bin/bash
# Install deps
sudo apt-get update
sudo apt-get install -y build-essential libreadline-gplv2-dev libncursesw5-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev python3-dev libssl1.0-dev python-netlib libjpeg62-turbo-dev libxml2-dev libxslt1-dev python-dev libnetfilter-queue-dev

# Setup Python deps
sudo pip3.6 install mitmproxy==4.0.4 emoji netaddr
sudo pip3.6 install -r requirements.txt
sudo pip3.6 install service_identity --upgrade
