#Ggl8QRDuWiJucOxgzSxz
from elasticsearch import Elasticsearch
import io
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic","Ggl8QRDuWiJucOxgzSxz"))
print(es.ping())

#delete elasticsearch index by reading input file

with io.open("input.txt","r",encoding="utf-8") as f1:
    data=f1.read()
    f1.close()
data=data.split("\n")
for index in data:
    try:
        response=es.indices.delete(index=index)
        print(response)
    except Exception as e:
        print("error occured while deleting index:" + index + " ___with exact error: " + str(e))