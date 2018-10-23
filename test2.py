from mitmproxy.master import Master
from mitmproxy import options, proxy
from mitmproxy.proxy.server import ProxyServer
opts = options.Options(listen_host='0.0.0.0', listen_port=8081, mode='transparent')
config = proxy.ProxyConfig(opts)
server = ProxyServer(config)
server.allow_reuse_address = True
serverInstance = Master(opts=opts)
