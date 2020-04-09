# pip install python-nmap
# pip install pyreadline - for autocomplete
# python nmap-scanner.py 127.0.0.1

import nmap
import sys

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080] # some famous service ports
scan_v = nmap.PortScanner()

print("Scanning ",target," for ports 21,22,80,139,443,8080")

for port in ports:
	portscan = scan_v.scan(target, str(port))
	print("Port ",port," is ",portscan['scan'][target]['tcp'][port]['state'])

print("Host ",target," is ",portscan['scan'][target]['status']['state'])