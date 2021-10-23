
#search elasticsearch index
from elasticsearch import Elasticsearch

es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic","Ggl8QRDuWiJucOxgzSxz"))
print(es.ping())

#search specific index
index="hr"
try:
    response=es.search(index=index)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))

#search index based on pattern
index="october_*"
try:
    response=es.search(index=index)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))



