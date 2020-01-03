#!/usr/bin/env python3.5
from logging import getLogger,ERROR
getLogger('scapy.runtime').setLevel(ERROR)

"""
Author : Shane W. Scott - sscott@govanguard.com GoVanguard Inc.
Licence : GPL v3

Description:
    WiFi-Pickle - Framework for Rogue Wi-Fi Access Point Attack.

Copyright:
    Copyright (C) 2018-2019 Shane W. Scott GoVanguard Inc.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

from sys import argv,exit,version_info
import core.utility.constants as C

if __name__ == '__main__':
    from core.loaders.checker.depedences import check_dep_pickle
    from PyQt4 import QtGui
    from core.utility.application import ApplicationLoop
    from core.main import Initialize
    from core.loaders.checker.networkmanager import CLI_NetworkManager, UI_NetworkManager
    from core.utility.collection import SettingsINI

    check_dep_pickle()
    from os import getuid
    if not getuid() == 0:
        exit('[{}!{}] WiFi-Pickle must be run as root.'.format(C.RED,C.ENDC))

    app = ApplicationLoop(argv)
    if app.isRunning():
        QtGui.QMessageBox.warning(None,'Multiple Instances Warning','WiFi-Pickle is already running. Be aware that multiple instances could produce unusual behavior.')

    print('Loading GUI...')
    main = Initialize()
    main.setWindowIcon(QtGui.QIcon('icons/pickle2.svg'))
    main.center()
    # check if Wireless connection
    conf = SettingsINI(C.CONFIG_INI)
    if  conf.get_setting('accesspoint','checkConnectionWifi',format=bool):
        networkcontrol = CLI_NetworkManager() # add all interface avaliable for exclude
        main.networkcontrol = networkcontrol
        if networkcontrol.run():
            if  networkcontrol.isWiFiConnected() and len(networkcontrol.ifaceAvaliable) > 0:
                settings = UI_NetworkManager(main)
                settings.setWindowIcon(QtGui.QIcon('icons/pickle2.svg'))
                settings.show()
                exit(app.exec_())
    main.show()

    print('WiFi-Pickle Running!')
    exit(app.exec_())
