WiFi-Pickle (https://govanguard.io)
==

## Authors:
Shane Scott

## About legion
Based on WiFi-Pumpkin, WiFi-Pickle is a rogue WiFi access point attacks.

WiFi-Pickle is written in Python 3.6, has been partially ported from PyQt4 to PyQt5, and no longer uses anchient and arcane libraries. 

Tested on Ubuntu, Parrot Security OS, and Windows Subsystem for Linux. Some features do not work on WSL and not all wireless adapters are compatible.

Note that some of the plugins are not yet rewritten and some of the attacks, such as SSL Strip, seem to be ineffective at this time. They may be based on exploits that are patched in SSL, but I didn't dig into it yet.

<img src="https://raw.githubusercontent.com/GoVanguard/legion/master/legion.png" width="1000"></img>

## Installation
```
git clone https://github.com/GoVanguard/wifi-pickle.git
```

## Recommended Python Version
WiFi-Pickle supports Python 3.6+. It won't run in anything below Python 3.6. Don't even bother trying.

## Dependencies
* Ubuntu or variant
* Python 3.6+
* mitmproxy 4.0.3+
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
Note: Deps will be installed automatically.

## License
WiFi-Pickle is licensed under the GNU General Public License v3.0.

## Credits
Marcos Nesster - PocL4bs Team (WiFi-Pumpkin)
