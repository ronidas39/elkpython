#Ggl8QRDuWiJucOxgzSxz
from elasticsearch import Elasticsearch
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic","Ggl8QRDuWiJucOxgzSxz"))
print(es.ping())

#search and display the index names based on the given search pattern
index_pattern="october_*"
response=es.indices.get_alias(index_pattern)
if(len(response)>0):
    for index in response:
        delete_response=es.indices.delete(index=index)
        print(delete_response)
else:
    print("no index has been found for the given search pattern")