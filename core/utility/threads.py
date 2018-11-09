import logging
import signal
import argparse
import threading
from re import search
from sys import stdout
from time import asctime
from os import path,stat,getpgid,setsid,killpg,devnull
from twisted.web import http
from twisted.internet import reactor
from twisted.internet.defer import DebugInfo
del DebugInfo.__del__
from core.utils import setup_logger,Refactor
from subprocess import (Popen,PIPE,STDOUT)
from PyQt4.QtCore import QThread,pyqtSignal,SIGNAL,pyqtSlot,QProcess,QObject,SLOT
from PyQt4.QtGui import QMessageBox
from multiprocessing import Process,Manager
import core.utility.constants as C

from compat import *

"""
Description:
    This program is a core for wifi-pickle.py. file which includes functionality
    for threads core program.

Copyright:
    Copyright (C) 2015-2016 Marcos Nesster P0cl4bs Team
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


class ProcessThreadScanner(threading.Thread):
    ''' thread for run airodump-ng backgroung and get data'''
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        self.process = Popen(self.cmd,stdout=PIPE,stderr=STDOUT)
        for line in iter(self.process.stdout.readline, b''):
            pass
    def stop(self):
        if self.process is not None:
            self.process.terminate()

class ThreadPopen(QThread):
    def __init__(self,cmd):
        QThread.__init__(self)
        self.cmd = cmd
        self.process = None

    def getNameThread(self):
        return '[New Thread {} ({})]'.format(self.currentThreadId(),self.objectName())

    def run(self):
        print('[New Thread {} ({})]'.format(self.currentThreadId(),self.objectName()))
        self.process = Popen(self.cmd,stdout=PIPE,stderr=STDOUT,close_fds=True)
        for line in iter(self.process.stdout.readline, b''):
            self.emit(SIGNAL('Activated( PyQt_PyObject )'),line.rstrip())

    def stop(self):
        print('Stop thread:' + self.objectName())
        if self.process is not None:
            self.process.terminate()
            self.process = None

class ThRunDhcp(QThread):
    ''' thread: run DHCP on background fuctions'''
    sendRequest = pyqtSignal(object)
    def __init__(self,args,session):
        QThread.__init__(self)
        self.args    = args
        self.session = session
        self.process = None

    def getNameThread(self):
        return '[New Thread {} ({})]'.format(self.currentThreadId(),self.objectName())

    def run(self):
        self.process = Popen(self.args,
        stdout=PIPE,stderr=STDOUT,preexec_fn=setsid)
        print('[New Thread {} ({})]'.format(self.process.pid,self.objectName()))
        setup_logger('dhcp', C.LOG_DHCP,self.session)
        loggerDhcp = logging.getLogger('dhcp')
        loggerDhcp.info('---[ Start DHCP '+asctime()+']---')
        for line,data in enumerate(iter(self.process.stdout.readline, b'')):
            data = data.decode()
            if 'DHCPREQUEST for' in data.rstrip():
                self.sendRequest.emit(data.split())
            elif 'DHCPACK on' in data.rstrip():
                self.sendRequest.emit(data.split())
            elif 'reuse_lease' in data.rstrip():
                self.sendRequest.emit(data.split())
            loggerDhcp.info(data.rstrip())

    def stop(self):
        print('Thread::[{}] successfully stopped.'.format(self.objectName()))
        if self.process is not None:
            killpg(getpgid(self.process.pid), signal.SIGTERM)


class ThreadScan(QThread):
    def __init__(self,gateway):
        QThread.__init__(self)
        self.gateway = gateway
        self.result = ''
    def run(self):
        try:
            nm = PortScanner()
            a=nm.scan(hosts=self.gateway, arguments='-sU --script nbstat.nse -O -p137')
            for k,v in a['scan'].iteritems():
                if str(v['status']['state']) == 'up':
                    try:
                        ip = str(v['addresses']['ipv4'])
                        hostname = str(v['hostscript'][0]['output']).split(',')[0]
                        hostname = hostname.split(':')[1]
                        mac = str(v['hostscript'][0]['output']).split(',')[2]
                        if search('<unknown>',mac):mac = '<unknown>'
                        else:mac = mac[13:32]
                        self.result = ip +'|'+mac.replace('\n','')+'|'+hostname.replace('\n','')
                        self.emit(SIGNAL('Activated( PyQt_PyObject )'),self.result)
                    except :
                        pass
        except NameError:
            QMessageBox.information(self,'error module','the module Python-nmap not installed')

class ThreadFastScanIP(QThread):
    sendDictResultscan = pyqtSignal(object)
    def __init__(self,gateway,iprange,parent=None):
        super(ThreadFastScanIP, self).__init__(parent)
        self.ip_range = str(iprange).split('-')
        self.workingThread = True
        self.gatewayNT = gateway[:len(gateway)-len(gateway.split('.').pop())]
        self.setTerminationEnabled(True)

    def run(self):
        self.jobs = []
        self.manager = Manager()
        on_ips = self.manager.dict()
        for n in xrange(int(self.ip_range[0]),int(self.ip_range[1])):
            ip='%s{0}'.format(n)%(self.gatewayNT)
            if not self.workingThread: break
            p = Process(target=self.working,args=(ip,on_ips))
            self.jobs.append(p)
            p.start()
        for proc in self.jobs:
            proc.join()
            proc.terminate()
        self.sendDictResultscan.emit(on_ips)

    def working(self,ip,lista):
        with open(devnull, 'wb') as limbo:
            result=Popen(['ping', '-c', '1', '-n', '-W', '1', ip],
            stdout=limbo, stderr=limbo).wait()
            if not result:
                if Refactor.get_mac(ip) == None:
                    lista[ip] = ip + '|' + 'not found'
                else:
                    lista[ip] = ip + '|' + Refactor.get_mac(ip)
    def stop(self):
        self.workingThread = False


class ProcessThread(QObject):
    _ProcssOutput = pyqtSignal(object)
    def __init__(self,cmd ,directory_exec=None):
        QObject.__init__(self)
        self.directory_exec = directory_exec
        self.cmd = cmd

    def getNameThread(self):
        return '[New Thread {} ({})]'.format(self.procThread.pid(),self.objectName())

    @pyqtSlot()
    def readProcessOutput(self):
        self.data = str(self.procThread.readAllStandardOutput())
        self._ProcssOutput.emit(self.data)

    def start(self):
        self.procThread = QProcess(self)
        self.procThread.setProcessChannelMode(QProcess.MergedChannels)
        if self.directory_exec:
            self.procThread.setWorkingDirectory(self.directory_exec)
        QObject.connect(self.procThread, SIGNAL('readyReadStandardOutput()'), self, SLOT('readProcessOutput()'))
        self.procThread.start(list(dict(self.cmd).keys())[0],self.cmd[list(dict(self.cmd).keys())[0]])
        print('[New Thread {} ({})]'.format(self.procThread.pid(),self.objectName()))

    def stop(self):
        print('Thread::[{}] successfully stopped.'.format(self.objectName()))
        if hasattr(self,'procThread'):
            self.procThread.terminate()
            self.procThread.waitForFinished()
            self.procThread.kill()

class ThreadMitmProxy(ProcessThread):
    def __init__(self, cmd, plugins={}, directory_exec=None):
        QThread.__init__(self)
        self.plugins  = plugins
        self.directory_exec = directory_exec
        self.cmd = cmd

    def disablePlugin(self,name, status):
        ''' disable plugin by name '''
        plugin_on = []
        if status:
            for plugin in self.plugins:
                plugin_on.append(self.plugins[plugin].Name)
            if name not in plugin_on:
                for p in self.plugin_classes:
                    pluginconf = p()
                    if  pluginconf.Name == name:
                        self.plugins[name] = pluginconf
                        self.plugins[name].getInstance()._activated = True
                        print('MITM Proxy::{0:17} status:On'.format(name))
        else:
            print('MITM Proxy::{0:17} status:Off'.format(name))
            self.plugins.pop(self.plugins[name].Name)

class ProcessHostapd(QObject):
    statusAP_connected = pyqtSignal(object)
    statusAPError = pyqtSignal(object)
    def __init__(self,cmd,session):
        QObject.__init__(self)
        self.cmd         = cmd
        self.session     = session
        self.errorAPDriver = ('AP-DISABLED',
        'Failed to initialize interface',
        'nl80211 driver initialization failed.',
        'errors found in configuration file')

    def getNameThread(self):
        return '[New Thread {} ({})]'.format(self.procHostapd.pid(),self.objectName())

    @pyqtSlot()
    def read_OutputCommand(self):
        self.data = str(self.procHostapd.readAllStandardOutput())
        if 'AP-STA-DISCONNECTED' in self.data.rstrip() or 'inactivity (timer DEAUTH/REMOVE)' in self.data.rstrip():
            self.statusAP_connected.emit(self.data.split()[2])
        ### Add back here
        self.log_hostapd.info(self.data)
        for error in self.errorAPDriver:
            if self.data.find(error) != -1:
                return self.statusAPError.emit(self.data)

    def start(self):
        self.makeLogger()
        self.procHostapd = QProcess(self)
        self.procHostapd.setProcessChannelMode(QProcess.MergedChannels)
        QObject.connect(self.procHostapd, SIGNAL('readyReadStandardOutput()'), self, SLOT('read_OutputCommand()'));
        self.procHostapd.start(list(dict(self.cmd).keys())[0],self.cmd[list(dict(self.cmd).keys())[0]])
        print('[New Thread {} ({})]'.format(self.procHostapd.pid(),self.objectName()))

    def makeLogger(self):
        setup_logger('hostapd', C.LOG_HOSTAPD, self.session)
        self.log_hostapd = logging.getLogger('hostapd')

    def stop(self):
        print('Thread::[{}] successfully stopped.'.format(self.objectName()))
        if hasattr(self,'procHostapd'):
            QObject.disconnect(self.procHostapd,
            SIGNAL('readyReadStandardOutput()'), self, SLOT('read_OutputCommand()'))
            self.procHostapd.terminate()
            self.procHostapd.waitForFinished()
            self.procHostapd.kill()

class ThreadReactor(QThread):
    '''Thread: run reactor twisted on brackground'''
    def __init__(self,parent=None):
        super(ThreadReactor, self).__init__(parent)
    def run(self):
        reactor.run(installSignalHandlers=False)
    def stop(self):
        reactor.callFromThread(reactor.stop)
