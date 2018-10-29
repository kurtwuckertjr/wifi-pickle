#!/bin/bash
# Install deps
sudo apt-get update
sudo apt-get install -y build-essential libreadline-gplv2-dev libncursesw5-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev python3-dev libssl1.0-dev python-netlib libjpeg62-turbo-dev libxml2-dev libxslt1-dev python-dev libnetfilter-queue-dev

cd /tmp

# Setup Python3.5
wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
tar xzf Python-3.6.6.tgz
cd Python-3.6.6/
./configure --enable-optimizations --enable-ipv6 --with-ensurepip=install
sudo make altinstall
cd ..

# Setup SIP and PyQt4
wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.3/PyQt4_gpl_x11-4.12.3.tar.gz
tar zxvf sip-4.19.13.tar.gz 
tar zxvf PyQt4_gpl_x11-4.12.3.tar.gz
cd sip-4.19.13/
python3.6 configure.py -d /usr/local/lib/python3.6/site-packages --sip-module PyQt4.sip --target-py-version=3.6
make
sudo make install
make clean
cd ..
cd PyQt4_gpl_x11-4.12.3/
python3.6 configure-ng.py -d /usr/local/lib/python3.6/site-packages --target-py-version=3.6
make
sudo make install
make clean

# Setup Python deps
sudo pip3.6 install mitmproxy==4.0.4 emoji netaddr
sudo pip3.6 install -r requirements.txt
sudo pip3.6 install service_identity --upgrade
