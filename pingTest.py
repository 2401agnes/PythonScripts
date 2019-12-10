import os
import ipaddress
import platform
import subprocess as sp
f_host = input("Enter the ip address you wish to test: ")
ran = int(input("Enter no ips: "))
nex_host = f_host
for i in range(ran):
    pingTest = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    # the os opens and reads the ping results and compares  is there is TTL inside the results
    results = os.popen("ping " + pingTest + " " + nex_host).read()
    if "TTL=" in results:
        print(nex_host, 'is up!')
    else:
        print(nex_host, 'is down !')
    n_host = ipaddress.ip_address(nex_host) + 1
    nex_host = str(n_host)
