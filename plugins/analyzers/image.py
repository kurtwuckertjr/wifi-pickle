from random import randint
from scapy.all import *
from plugins.analyzers.default import PSniffer
from urllib.request import urlretrieve
from scapy_http import http
from os.path import splitext
from string import ascii_letters

class ImageCap(PSniffer):
    ''' capture image content http'''
    _activated     = False
    _instance      = None
    meta = {
        'Name'      : 'imageCap',
        'Version'   : '1.0',
        'Description' : 'capture image content http',
        'Author'    : 'Pickle-Dev',
    }
    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value

    @staticmethod
    def getInstance():
        if ImageCap._instance is None:
            ImageCap._instance = ImageCap()
        return ImageCap._instance

    def filterPackets(self,pkt):
        if not pkt.haslayer(http.HTTPRequest):
            return

        httpLayer = pkt.getlayer(http.HTTPRequest)
        ipLayer = pkt.getlayer(IP)

        xt = ['.svg', '.gif', '.png', '.jpg']
        filename, fileExtension = splitext(httpLayer.fields['Path'])
        filename = filename.decode('utf-8')
        fileExtension = fileExtension.decode('utf-8')
        if fileExtension in xt:
            print('Plugin imageCap: {}'.format(filename))
            sessionName = self.session.decode('utf-8')
            targetFileName = 'logs/ImagesCap/%s_%s%s' % (sessionName, self.randomChar(5), fileExtension)
            hostName = httpLayer.fields['Host']
            hostName = hostName.decode('utf-8')
            imagePath = httpLayer.fields['Path']
            imagePath = imagePath.decode('utf-8')
            urlretrieve('http://{}{}'.format(hostName, imagePath), targetFileName)
            self.output.emit({'image': targetFileName})

    def randomChar(self,y):
           return ''.join(random.choice(ascii_letters) for x in range(y))
