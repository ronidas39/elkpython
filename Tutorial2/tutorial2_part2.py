#index creation in bulk using input file
from elasticsearch import Elasticsearch
import io
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic","Ggl8QRDuWiJucOxgzSxz"))
print(es.ping())
#index creation in bulk using input file
with io.open("input.txt","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
data=data.split("\n")
for index in data:
    response=es.indices.create(index=index)
    print(response)

