#!/bin/bash

sysctl -w net.ipv4.ip_forward=0
sysctl -w net.ipv6.conf.all.forwarding=f
sysctl -w net.ipv4.conf.all.send_redirects=1

ps aux | grep mitmproxy | grep python | awk '{print $2}'| xargs kill -9
