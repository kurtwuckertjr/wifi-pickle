from scapy.all import *
from plugins.analyzers.default import PSniffer
from urllib.request import urlretrieve
from scapy_http import http
from os.path import splitext
from string import ascii_letters
from compat import *

class ImageCapture(PSniffer):
    '''TCP Proxy plugin to capture image content from TCP Proxy monitored ports'''
    _activated     = False
    _instance      = None
    meta = {
        'Name'      : 'imageCapture',
        'Version'   : '2.0',
        'Description' : 'TCP Proxy plugin to capture image content from TCP Proxy monitored ports',
        'Author'    : 'Shane W. Scott',
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value

    @staticmethod
    def getInstance():
        if ImageCapture._instance is None:
            ImageCapture._instance = ImageCapture()
        return ImageCapture._instance

    def filterPackets(self,pkt):
        if not pkt.haslayer(http.HTTPRequest):
            return

        httpLayer = pkt.getlayer(http.HTTPRequest)
        ipLayer = pkt.getlayer(IP)

        xts = ['svg', 'gif', 'png', 'jpg']
        try:
            imageType = httpLayer.fields['Accept']
            imageType = imageType.decode('utf-8')
        except:
            return
        imageUrl = httpLayer.fields['Path']
        imageUrl = imageUrl.decode('utf-8')
        fileExtension = None

        for xt in xts:
            if xt in imageType:
                fileExtension = xt

        if fileExtension:
            print('Plugin imageCap: {}'.format(imageUrl))
            sessionName = self.session
            targetFileName = 'logs/ImagesCap/%s_%s.%s' % (str(sessionName), str(randomChar(5)), str(fileExtension))
            hostName = httpLayer.fields['Host']
            hostName = hostName.decode('utf-8')
            try:
                try:
                    urlretrieve('http://{}{}'.format(hostName, imageUrl), targetFileName)
                except urllib.error.HTTPError:
                    urlretrieve('https://{}{}'.format(hostName, imageUrl), targetFileName)
                self.output.emit({'image': targetFileName})
            except Exception as e:
                print('Plugin imageCap error: {}'.format(str(e)))
