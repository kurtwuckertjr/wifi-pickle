#!/bin/bash

sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv6.conf.all.forwarding=1
sysctl -w net.ipv4.conf.all.send_redirects=0

mitmproxy --listen-host='0.0.0.0' -p 8080 --mode transparent --no-showhost --script core/helpers/sslstrip.py 2>&1> mitmproxy-out
