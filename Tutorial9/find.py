import requests

response=requests.get("http://localhost:9200/test_index_using_api/_doc/100000?_source=false&pretty",auth=("elastic", "9R-bViTHVn8xp_wJtDPh"))
found=response.json()["found"]
if found:
    print("doc id is present")
else:
    print("doc id is not present")
