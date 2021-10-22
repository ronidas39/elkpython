from elasticsearch import Elasticsearch
##setup connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=('elastic', 'Ggl8QRDuWiJucOxgzSxz'))
print(es.ping())
##create index
#es.indices.create(index="tutorial2-16_10_2021")
##display all indices
indices=es.indices.get_alias()
for index in indices:
    print(index)