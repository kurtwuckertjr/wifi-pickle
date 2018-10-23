#!/bin/bash

sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv6.conf.all.forwarding=1

sysctl -w net.ipv4.conf.all.send_redirects=0

#iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 80 -j REDIRECT --to-port 8081
#iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 443 -j REDIRECT --to-port 8081
#ip6tables -t nat -A PREROUTING -i wlan1 -p tcp --dport 80 -j REDIRECT --to-port 8081
#ip6tables -t nat -A PREROUTING -i wlan1 -p tcp --dport 443 -j REDIRECT --to-port 8081

mitmproxy --listen-host='0.0.0.0' -p 8081 --mode transparent --no-showhost --scripts=test.py  2>&1> mitmproxy-out

