#create index using elasticsearch api

import requests

response=requests.put("http://localhost:9200/test_index_using_api",auth=("elastic", "Ggl8QRDuWiJucOxgzSxz"))
print(response.text)