import requests
import re
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
lines = []
hack = []
print('enter all urls separated by new line:-')
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
    headers={'X-Forwarded-Host': 'exploit-ac.com'}
    try:
        r = requests.get(url,timeout=10, verify=False, headers=headers)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
    	print ("OOps: Something Else")
    except requests.exceptions.HTTPError as errh:
    	print ("Http Error:")
    except requests.exceptions.ConnectionError as errc:
    	print ("Error Connecting:")
    except requests.exceptions.Timeout as errt:
    	print ("Timeout Error:")     
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
        	print("status error", y)
for i in range(0,y):
    x=lines[i]
    url= "https://"+x
    headers={'X-Forwarded-For': 'exploit-ac.com'}
    try:
        r = requests.get(url,timeout=10, verify=False, headers=headers)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
    	print ("OOps: Something Else")
    except requests.exceptions.HTTPError as errh:
    	print ("Http Error:")
    except requests.exceptions.ConnectionError as errc:
    	print ("Error Connecting:")
    except requests.exceptions.Timeout as errt:
    	print ("Timeout Error:")     
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
        	print("status error", y)
for i in range(0,y):
    x=lines[i]
    url= "https://"+x
    headers={'X-Host': 'exploit-ac.com'}
    try:
        r = requests.get(url,timeout=10, verify=False, headers=headers)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
    	print ("OOps: Something Else")
    except requests.exceptions.HTTPError as errh:
    	print ("Http Error:")
    except requests.exceptions.ConnectionError as errc:
    	print ("Error Connecting:")
    except requests.exceptions.Timeout as errt:
    	print ("Timeout Error:")     
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
        	print("status error", y)
print(hack)
