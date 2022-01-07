import json
dict={}
key=[]
with open("textpriya.txt") as file:
    for i in file:
        k=i.split()
        value=" "
        for j in range(len(k)):
            if k[0] not in  key:
                key.append(k[0])
            else:
                value=value+" "+(k[j])
        dict[k[0]]=value

k=open("txt_to_json.json","w")
json.dump(dict,k,indent=4)

k.close()
