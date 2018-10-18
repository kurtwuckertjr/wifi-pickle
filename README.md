WiFi-Pickle (https://govanguard.io)
==

## Authors:
Shane Scott

## About legion
Based on WiFi-Pumpkin, WiFi-Pickle is a rogue WiFi access point attacks.

WiFi-Pickle is written in Python 3, has been ported from PyQt4 to PyQt5, and no longer uses anchient and arcane libraries. 

Tested on Ubuntu, Parrot Security OS, and Windows Subsystem for Linux. Some features do not work on WSL and not all wireless adapters are compatible.

<img src="https://raw.githubusercontent.com/GoVanguard/legion/master/legion.png" width="1000"></img>

## Installation
```
git clone https://github.com/GoVanguard/wifi-pickle.git
```

## Recommended Python Version
WiFi-Pickle supports Python 3.5. It won't work under Python 3.6 yet. Don't even bother trying.

## Dependencies
* Ubuntu or variant or WSL (Windows Subsystem for Linux)
* Python 3.5
* mitmproxy 4.0+
* PyQT5
* six

## Usage
Run startWifiPickle start script to launch WiFi-Pickle. You may first have to grant yourself the permission to execute the script, which can either be done by right clicking it and selecting Properties and enabling Execute permissions, or:
```
chmod +x startWifiPickle.sh
```

Then run startLegion as root:
```
sudo ./startWifiPickle.sh
```
Note: Deps will be installed automatically.
Note: If you need to install Python3.5 run ./deps/installPython35.sh

## License
WiFi-Pickle is licensed under the GNU General Public License v3.0.

## Credits
Marcos Nesster - PocL4bs Team (WiFi-Pumpkin)
