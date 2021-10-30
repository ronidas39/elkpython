#search specific index using elasticsearch api

import requests
index_name="company"
response=requests.get("http://localhost:9200/"+index_name,auth=("elastic", "Ggl8QRDuWiJucOxgzSxz"))
keys=response.json().keys()
found=0
for key in keys:
    if key == index_name:
        found=1
        break
if(found==1):
    print(f"{index_name} has been found")
else:
    print(f"{index_name} has not been found")

