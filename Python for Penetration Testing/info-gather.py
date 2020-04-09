import sys
import requests
import socket
import json

if len(sys.argv) < 2:
	print("Usage: "+sys.srgv[0]+"<url>")

req = requests.get("https://"+sys.argv[1])
print(str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("The IP address of "+sys.argv[1]+" is "+gethostby_)

#ipinfo.io

req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.loads(req_two.text)

print("Location : "+resp_['loc'])
print("Region : "+resp_['region'])
print("City : "+resp_['city'])
print("Country : "+resp_['country'])