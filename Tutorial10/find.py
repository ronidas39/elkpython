import requests

response=requests.get("http://localhost:9200/test_index_using_api/_source/100?_source_includes=ip_address&pretty",auth=("elastic", "9R-bViTHVn8xp_wJtDPh"))
print(response.json())