#!/bin/bash
# Setup Python deps
sudo pip3.6 install mitmproxy==4.0.4 emoji netaddr
sudo pip3.6 install -r requirements.txt
sudo pip3.6 install service_identity --upgrade
