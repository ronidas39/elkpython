import requests
import io


with io.open("weblog.csv","r",encoding="utf-8") as f1:
    data=f1.read()
    f1.close()
lines=data.split("\n")[1:]
i=1
for line in lines:
    ip=line.split(",")[0]
    time=line.split(",")[1]
    url=line.split(",")[2]
    status=line.split(",")[3]
    url="http://localhost:9200/"
    headers={
    "Content-Type":"application/json",
    }
    json_data={
        "ip_address":ip,
        "timesmtap":time,
        "url":url,
        "status":status
    }
    response=requests.put(url+"test_index_using_api/_doc/"+str(i)+"?pretty",headers=headers,json=json_data,auth=("elastic", "9R-bViTHVn8xp_wJtDPh"))
    print(f"doc #{i} is added")
    i=i+1