import requests

url="http://localhost:9200/"
headers={
    "Content-Type":"application/json",
}
json_data={
    "message":"this is added by python and rest api and id 2"
}
response=requests.put(url+"test_index_using_api/_doc/2?pretty",headers=headers,json=json_data)
print(response)
