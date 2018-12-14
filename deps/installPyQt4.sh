#!/bin/bash
cd /tmp

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
python3.6 configure-ng.py -d /usr/local/lib/python3.6/site-packages --target-py-version=3.6 -silent -release -opensource -no-compile-examples -nomake examples -nomake t
ests -no-qml-debug -confirm-license
make
sudo make install
make clean
