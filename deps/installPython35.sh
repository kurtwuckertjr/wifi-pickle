#!/bin/bash
# Install deps
sudo apt-get update
sudo apt-get install -y build-essential libreadline-gplv2-dev libncursesw5-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev python3-dev libssl1.0-dev python-netlib libjpeg62-turbo-dev

cd /tmp

# Setup Python3.5
wget https://www.python.org/ftp/python/3.5.5/Python-3.5.5.tgz
tar xzf Python-3.5.5.tgz
cd Python-3.5.5/
./configure --enable-optimizations --enable-ipv6 --with-ensurepip=install
sudo make altinstall
cd ..

# Setup SIP and PyQt4
wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.3/PyQt4_gpl_x11-4.12.3.tar.gz
tar zxvf sip-4.19.13.tar.gz 
tar zxvf PyQt4_gpl_x11-4.12.3.tar.gz
cd sip-4.19.13/
python3.5 configure.py -d /usr/local/lib/python3.5/site-packages --sip-module PyQt4.sip --target-py-version=3.5
make
sudo make install
make clean
cd ..
cd PyQt4_gpl_x11-4.12.3/
python3.5 configure-ng.py -d /usr/local/lib/python3.5/site-packages --target-py-version=3.5
make
sudo make install
make clean

# Setup Python deps
sudo pip3.5 install mitmproxy==0.18.2 emoji netaddr
sudo pip3.5 install -i requirements.txt
sudo pip3.5 install service_identity --upgrade
