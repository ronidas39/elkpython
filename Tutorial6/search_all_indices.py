import requests
import json

##elastic', 'Ggl8QRDuWiJucOxgzSxz'
#search all indices using elasticsearch api
import requests
response=requests.get("http://localhost:9200/_cat/indices?format=json&pretty",auth=("elastic", "Ggl8QRDuWiJucOxgzSxz"))
data=response.json()
[print(row["index"])for row in data]