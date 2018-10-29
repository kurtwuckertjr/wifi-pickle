domains.cfg (or dominios.cfg): resolve all hosts for the listed domains with the listed IP

    Ex: .facebook.com 1.2.3.4 .fbi.gov 1.2.3.4

spoof.cfg : Spoof a host with a ip

    Ex: www.nsa.gov 127.0.0.1

nospoof.cfg: Send always a legit response when asking for these hosts.

    Ex. mail.google.com

nospoofto.cfg: Don't send fake responses to the IPs listed there.

    Ex: 127.0.0.1 4.5.6.8

victims.cfg: If not empty, only send fake responses to these IP addresses.

    Ex: 23.66.163.36 195.12.226.131

resolv.conf: DNS server to forward the queries.

    Ex: nameserver 8.8.8.8

