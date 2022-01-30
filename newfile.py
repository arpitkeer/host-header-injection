import requests
import re
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
lines = []
hack = []
print('enter all urls:-')
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
    headers={'X-Forwarded-Host': 'exploit-ac.com', 'X-Forwarded-For': 'exploit-ac.com', 'X-Client-IP': 'exploit-ac.com', 'X-Remote-IP': 'exploit-ac.com', 'X-Remote-Addr': 'exploit-ac.com', 'X-Host': 'exploit-ac.com'}
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
 	   	    b=(re.search('exploit-ac.com', z, re.IGNORECASE))
 	   	    if b:
 	   	    	print("nice")
 	   	    	print(url)
 	   	    	hack += [url]
 	   	    else:
 	   	    	print("sorry")
    else:
        	print("status error")
print(hack)
