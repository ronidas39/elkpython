##Ggl8QRDuWiJucOxgzSxz
#index creation in bulk using sequence number
from elasticsearch import Elasticsearch
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic","Ggl8QRDuWiJucOxgzSxz"))
print(es.ping())

#create index with sequence

index_basename="october"
for i in  range(1,11):
    response=es.indices.create(index=index_basename+"_"+str(i))
    print(response)

