from re import search
import modules as GUIs
from core.main import QtGui,QtCore
from core.utils import Refactor
from collections import OrderedDict
from core.widgets.pluginssettings import ResponderSettings

from compat import *
"""
Description:
    This program is a core for wifi-pickle.py. file which includes functionality
    for load plugins mitm attack and phishing module.

Copyright:
    Copyright (C) 2015-2017 Marcos Nesster P0cl4bs Team
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

class PopUpPlugins(QtGui.QVBoxLayout):
    ''' this module control all plugins to MITM attack'''
    sendSingal_disable = QtCore.pyqtSignal(object)
    def __init__(self,FSettings,main,parent=None):
        super(PopUpPlugins, self).__init__(parent)
        self.main_method = main
        self.FSettings = FSettings
        self.layout = QtGui.QVBoxLayout()
        self.layoutform = QtGui.QFormLayout()
        self.layoutproxy = QtGui.QVBoxLayout()
        self.GroupPlugins = QtGui.QGroupBox()
        self.GroupPluginsProxy = QtGui.QGroupBox()
        self.GroupPlugins.setTitle('plugins:')
        self.GroupPluginsProxy.setLayout(self.layoutproxy)
        self.GroupPlugins.setLayout(self.layoutform)

        self.check_netcreds     = QtGui.QCheckBox('net-creds ')
        self.check_responder    = QtGui.QCheckBox('Responder')
        self.check_tcpproxy     = QtGui.QCheckBox('TCP-Proxy')
        self.check_noproxy      = QtGui.QRadioButton('No Proxy')
        self.check_mitmproxy    = QtGui.QRadioButton('MITM Proxy (HTTP)')
        self.check_mitmproxyssl   = QtGui.QRadioButton('MITM Proxy (HTTP/HTTPS)')

        self.btnResponderSettings = QtGui.QPushButton('Change')
        self.btnResponderSettings.setIcon(QtGui.QIcon('icons/config.png'))
        #self.btnResponderSettings.clicked.connect(self.ConfigOBJBResponder)

        # set text description plugins
        self.check_mitmproxy.setObjectName('MITM Proxy 4.0.4. Forward HTTP only')
        self.check_mitmproxyssl.setObjectName('MITM Proxy 4.0.4. Forward HTTP and HTTPS')
        self.check_noproxy.setObjectName('No HTTP / HTTPS proxying')

        # desction plugin checkbox
        self.check_netcreds.setObjectName('Sniff passwords and hashes from an interface or pcap file.'
        ' coded by: Dan McInerney')
        self.check_tcpproxy.setObjectName('sniff for isntercept network traffic on UDP,TCP protocol.'
        ' get password,hash,image,etc...')
        self.check_responder.setObjectName('Responder an LLMNR, NBT-NS and MDNS poisoner. '
        'By default, the tool will only answer to File Server Service request, which is for SMB.')


        # table 1 for add plugins with QradioBtton
        self.THeadersPluginsProxy  = OrderedDict(
        [   ('Plugins',[self.check_noproxy, self.check_mitmproxy, self.check_mitmproxyssl]),
            ('Settings',[QtGui.QPushButton('None'), QtGui.QPushButton('None'), QtGui.QPushButton('None')]),
            ('Description',[self.check_noproxy.objectName(), self.check_mitmproxy.objectName(), self.check_mitmproxyssl.objectName()])
        ])

        # table 2 for add plugins with checkbox
        self.THeadersPlugins  = OrderedDict(
        [   ('Plugins',[self.check_tcpproxy, self.check_responder]),
            ('Settings',[QtGui.QPushButton('None'), self.btnResponderSettings]),
            ('Description',[self.check_tcpproxy.objectName(), self.check_responder.objectName()])
        ])

        self.tableplugins = QtGui.QTableWidget()
        self.tableplugins.setColumnCount(3)
        self.tableplugins.setRowCount(len(self.THeadersPluginsProxy['Plugins']))
        self.tableplugins.resizeRowsToContents()
        self.tableplugins.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.tableplugins.horizontalHeader().setStretchLastSection(True)
        self.tableplugins.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableplugins.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableplugins.verticalHeader().setVisible(False)
        self.tableplugins.verticalHeader().setDefaultSectionSize(23)
        self.tableplugins.setSortingEnabled(True)
        self.tableplugins.setHorizontalHeaderLabels(list(sorted(dict(self.THeadersPluginsProxy).keys())))
        self.tableplugins.horizontalHeader().resizeSection(0, 300)
        self.tableplugins.horizontalHeader().resizeSection(1, 190)
        self.tableplugins.resizeRowsToContents()

        self.tableplugincheckbox = QtGui.QTableWidget()
        self.tableplugincheckbox.setColumnCount(3)
        self.tableplugincheckbox.setRowCount(len(self.THeadersPlugins['Plugins']))
        self.tableplugincheckbox.resizeRowsToContents()
        self.tableplugincheckbox.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.tableplugincheckbox.horizontalHeader().setStretchLastSection(True)
        self.tableplugincheckbox.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableplugincheckbox.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableplugincheckbox.verticalHeader().setVisible(False)
        self.tableplugincheckbox.verticalHeader().setDefaultSectionSize(23)
        self.tableplugincheckbox.setSortingEnabled(True)
        self.tableplugincheckbox.setHorizontalHeaderLabels(list(sorted(dict(self.THeadersPlugins).keys())))
        self.tableplugincheckbox.horizontalHeader().resizeSection(0, 300)
        self.tableplugincheckbox.horizontalHeader().resizeSection(1, 190)
        self.tableplugincheckbox.resizeRowsToContents()

        # add all widgets in Qtable 1 plgins
        Headers = []
        for n, key in enumerate(list(sorted(dict(self.THeadersPluginsProxy).keys()))):
            Headers.append(key)
            for m, item in enumerate(self.THeadersPluginsProxy[key]):
                if type(item) == type(QtGui.QRadioButton()) or type(item) == type(QtGui.QPushButton()):
                    self.tableplugins.setCellWidget(m,n,item)
                else:
                    item = QtGui.QTableWidgetItem(item)
                    self.tableplugins.setItem(m, n, item)
        self.tableplugins.setHorizontalHeaderLabels(list(sorted(dict(self.THeadersPluginsProxy).keys())))

        # add all widgets in Qtable 2 plugin
        Headers = []
        for n, key in enumerate(list(sorted(dict(self.THeadersPlugins).keys()))):
            Headers.append(key)
            for m, item in enumerate(self.THeadersPlugins[key]):
                if type(item) == type(QtGui.QCheckBox()) or type(item) == type(QtGui.QPushButton()):
                    self.tableplugincheckbox.setCellWidget(m,n,item)
                else:
                    item = QtGui.QTableWidgetItem(item)
                    self.tableplugincheckbox.setItem(m, n, item)
        self.tableplugins.setHorizontalHeaderLabels(list(sorted(dict(self.THeadersPlugins).keys())))

        self.proxyGroup = QtGui.QButtonGroup()
        self.proxyGroup.addButton(self.check_mitmproxy)
        self.proxyGroup.addButton(self.check_mitmproxyssl)
        self.proxyGroup.addButton(self.check_noproxy)

        self.check_tcpproxy.clicked.connect(self.checkBoxTCPproxy)
        self.check_mitmproxy.clicked.connect(self.checkGeneralOptions)
        self.check_mitmproxyssl.clicked.connect(self.checkGeneralOptions)
        self.check_noproxy.clicked.connect(self.checkGeneralOptions)
        self.check_responder.clicked.connect(self.checkBoxResponder)

        self.layoutproxy.addWidget(self.tableplugins)
        self.layoutproxy.addWidget(self.tableplugincheckbox)
        self.layout.addWidget(self.GroupPluginsProxy)
        self.addLayout(self.layout)

    def get_disable_proxyserver(self):
        ''' set disable or activate plugin proxy '''
        self.check_noproxy.setChecked(True)
        self.tableplugincheckbox.setEnabled(True)
        self.sendSingal_disable.emit(self.check_noproxy.isChecked())
        self.checkBoxTCPproxy()

    # control checkbox plugins
    def checkGeneralOptions(self):
        ''' settings plugins proxy options and rules iptables '''
        self.unsetRules('mitmproxy')
        self.unsetRules('mitmproxyssl')
        self.FSettings.Settings.set_setting('plugins','mitmproxy_plugin',self.check_mitmproxy.isChecked())
        self.FSettings.Settings.set_setting('plugins','mitmproxyssl_plugin',self.check_mitmproxyssl.isChecked())
        self.FSettings.Settings.set_setting('plugins','noproxy',self.check_noproxy.isChecked())
        if self.check_mitmproxy.isChecked():
            self.main_method.set_proxy_statusbar('MITM-Proxy')
            self.main_method.MitmProxyTAB.tabcontrol.setEnabled(True)
            self.set_MitmProxyRule()
        elif self.check_mitmproxyssl.isChecked():
            self.main_method.set_proxy_statusbar('MITM-Proxy-SSL')
            self.main_method.MitmProxyTAB.tabcontrol.setEnabled(True)
            self.set_MitmProxySSLRule()
        elif self.check_noproxy.isChecked():
            self.main_method.set_proxy_statusbar('',disabled=True)
            self.main_method.MitmProxyTAB.tabcontrol.setEnabled(False)
            self.unsetRules('mitmproxy') 
            self.unsetRules('mitmproxyssl')
            self.tableplugincheckbox.setEnabled(True)
            self.checkBoxTCPproxy()

    def checkBoxTCPproxy(self):
        if self.check_tcpproxy.isChecked():
            self.FSettings.Settings.set_setting('plugins','tcpproxy_plugin',True)
            self.main_method.PacketSnifferTAB.tabcontrol.setEnabled(True)
            self.main_method.ImageCapTAB.TableImage.setEnabled(True)
        else:
            self.FSettings.Settings.set_setting('plugins','tcpproxy_plugin',False)
            self.main_method.PacketSnifferTAB.tabcontrol.setEnabled(False)
            self.main_method.ImageCapTAB.TableImage.setEnabled(False)

    def checkBoxResponder(self):
        if self.check_responder.isChecked():
            self.FSettings.Settings.set_setting('plugins','responder_plugin',True)
        else:
            self.FSettings.Settings.set_setting('plugins','responder_plugin',False)

    def optionsRules(self, serviceName):
        ''' add rules iptable by type plugins'''
        search = {
        'mitmproxy':
                    [
                        str('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8081'),
                    ],
        'mitmproxyssl':
                    [
                        str('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8081'),
                        str('iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8081')
                    ]
        }
        return search[serviceName]

    def setRules(self, serviceName, includeStockRules = True):
        items = []
        optionRulesResults = self.optionsRules(serviceName)
        if includeStockRules:
            for index in xrange(self.FSettings.ListRules.count()):
                items.append(str(self.FSettings.ListRules.item(index).text()))
        for rule in optionRulesResults:
            if rule in items:
                continue
            item = QtGui.QListWidgetItem()
            item.setText(rule)
            item.setSizeHint(QtCore.QSize(30,30))
            self.FSettings.ListRules.addItem(item) 

    def set_MitmProxyRule(self):
        self.setRules(serviceName = 'mitmproxy')

    def set_MitmProxySSLRule(self):
        self.setRules(serviceName = 'mitmproxyssl')

    def unsetRules(self, serviceName):
        ''' remove rules from Listwidget in settings widget'''
        optionRulesResults = self.optionsRules(serviceName)
        for index in xrange(self.FSettings.ListRules.count()):
            try:
                ruleData = str(self.FSettings.ListRules.item(index).text())
            except:
                self.FSettings.ListRules.takeItem(index)
                ruleData = '~' 
            if ruleData in str(optionRulesResults) or ruleData == '~':
                self.FSettings.ListRules.takeItem(index)
                continue
