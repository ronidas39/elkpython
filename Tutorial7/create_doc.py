import requests

url="http://localhost:9200/"
headers={
    "Content-Type":"application/json",
}
json_data={
    "message":"this is added by python and rest api and id 2",
     "count":10
}
response=requests.put(url+"test_index_using_api/_doc/3?pretty",headers=headers,json=json_data,auth=("elastic", "9R-bViTHVn8xp_wJtDPh"))
print(response)
