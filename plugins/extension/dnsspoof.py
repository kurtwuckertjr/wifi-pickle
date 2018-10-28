import re
from ast import literal_eval 
from plugins.extension.plugin import PluginTemplate


parse_host_header = re.compile(r"^(?P<host>[^:]+|\[.+\])(?::(?P<port>\d+))?$")

class DNSspoof(PluginTemplate):
    meta = {
        'Name'      : 'dnsspoof',
        'Version'   : '1.0',
        'Description' : 'DNS spoofing using MITMProxy',
        'Author'    : 'Shane Scott',
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = True
        self.getAllDomainToRedict()

    def getAllDomainToRedict(self):
        self.domains = self.config.get_all_childname('set_dnsspoof')
        for item in self.domains:
            if item.startswith('domain'):
                indomain = literal_eval(str(self.config.get_setting('set_dnsspoof',item)))
                self.dict_domain.update(indomain)


parse_host_header = re.compile(r"^(?P<host>[^:]+|\[.+\])(?::(?P<port>\d+))?$")

class Rerouter:
    def request(self, flow):
        if flow.client_conn.tls_established:
            flow.request.scheme = "https"
            sni = flow.client_conn.connection.get_servername()
            port = 443
        else:
            flow.request.scheme = "http"
            sni = None
            port = 80

        host_header = flow.request.host_header
        m = parse_host_header.match(host_header)
        if m:
            host_header = m.group("host").strip("[]")
            if m.group("port"):
                port = int(m.group("port"))

        flow.request.host_header = host_header
        flow.request.host = sni or host_header
        flow.request.port = port


addons = [Rerouter()]
