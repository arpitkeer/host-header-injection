import requests
import re
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
lines = []
Hackable = []
print('enter all urls(separated by new line:-')
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
y=len(lines)           
for i in range(0,y):
    x=lines[i]
    url= "https://"+x
    headers={'X-Forwarded-Host': 'exploit-ac631f9b1e71de74c0a80c8c01f10046.web-security-academy.net/'}
    try:
        r = requests.get(url,timeout=10, verify=False)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
    	print ("OOps: Something Else",err)
    except requests.exceptions.HTTPError as errh:
    	print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
    	print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
    	print ("Timeout Error:",errt)     
    y=r.status_code
    if y==200:
 	   	    z=r.text
 	   	    b=(re.search('exploit-ac631', z, re.IGNORECASE))
 	   	    if b:
 	   	    	print("nice")
 	   	    	print(url)
                        Hackable += [url]
 	   	    else:
 	   	    	print("sorry")
    else:
        	print("status error")
print(Hackable)
