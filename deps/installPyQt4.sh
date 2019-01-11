#!/bin/bash
testForPython=`python --version`
if [[ $testForPython == *"3.6"* ]]; then
    pythonBin='python'
else
    pythonBin='python3.6'
fi

cd /tmp

# Setup SIP and PyQt4
wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.3/PyQt4_gpl_x11-4.12.3.tar.gz
tar zxvf sip-4.19.13.tar.gz 
tar zxvf PyQt4_gpl_x11-4.12.3.tar.gz
cd sip-4.19.13/
$pythonBin configure.py -d /usr/local/lib/python3.6/site-packages --sip-module PyQt4.sip --target-py-version=3.6 
make
make install
make clean
cd ..
cd PyQt4_gpl_x11-4.12.3/
$pythonBin configure-ng.py --confirm-license -d /usr/local/lib/python3.6/site-packages --target-py-version=3.6
make
make install
make clean
