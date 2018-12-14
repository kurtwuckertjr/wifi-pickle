WiFi-Pickle (https://govanguard.io)
==
[![Build Status](https://travis-ci.com/GoVanguard/wifi-pickle.svg?branch=master)](https://travis-ci.com/GoVanguard/wifi-pickle)
[![Known Vulnerabilities](https://snyk.io/test/github/GoVanguard/wifi-pickle/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/GoVanguard/wifi-pickle?targetFile=requirements.txt)
[![Maintainability](https://api.codeclimate.com/v1/badges/260fbce0dd2d3d2ea216/maintainability)](https://codeclimate.com/github/GoVanguard/wifi-pickle/maintainability)

## Authors:
Shane Scott

## About Wifi-Pickle
Based on WiFi-Pumpkin, WiFi-Pickle is a rogue WiFi access point attacks.

WiFi-Pickle is written in Python 3.6, has been partially ported from PyQt4 to PyQt5, and no longer uses anchient and arcane libraries. 

Tested on Ubuntu, Parrot Security OS, and Windows Subsystem for Linux. Some features do not work on WSL and not all wireless adapters are compatible.

* HTTP / HTTPS + SSL Strip over MITMProxy 4.0.4
* TCP Proxy for 80, 443 and 8080. Image Capture for both HTTP and HTTPS where SSL Strip has been effective (not all sites are vulnerable to this)
* meatGlue DNS Proxy for DNS spoofing, rewrites, etc
* All deprecated, irrelevant and ineffective attacks removed

## Installation
```
git clone https://github.com/GoVanguard/wifi-pickle.git
```

## Recommended Python Version
WiFi-Pickle supports Python 3.6+. It won't run in anything below Python 3.6. Don't even bother trying.

## Dependencies
* Ubuntu or variant
* Python 3.6+
* mitmproxy 4.0.4+
* PyQT4 (Soon PyQT5)
* six, Twisted

## Usage
Run sudo ./startWifiPickle to launch WiFi-Pickle. You may first have to grant yourself the permission to execute the script, which can either be done by right clicking it and selecting Properties and enabling Execute permissions, or:
```
chmod +x startWifiPickle.sh
```

Then run startLegion as root:
```
sudo ./startWifiPickle.sh
```
Notes: 
* Requires Python 3.6. Installer for Python3.6 provided under ./deps if your distro doesn't have it
* Run installDeps.sh to install Python libraries
* Requires the exit line in console/master.py of MITMProxy 4.0.4 to be commented out

## License
WiFi-Pickle is licensed under the GNU General Public License v3.0.

## Credits
Marcos Nesster - PocL4bs Team (WiFi-Pumpkin)
