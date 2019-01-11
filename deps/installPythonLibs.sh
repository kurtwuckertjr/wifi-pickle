#!/bin/bash
# Setup Python deps
testForPip=`pip --version`
if [[ $testForPip == *"3.6"* ]]; then
    pipBin='pip'
else
    pipBin='pip3.6'
fi

$pipBin install -r requirements.txt
$pipBin install mitmproxy==4.0.4 emoji netaddr
$pipBin install service_identity --upgrade
