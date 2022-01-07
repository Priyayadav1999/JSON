import json

a={ '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}

x=open("sort_key.json","w")

json.dump(a,x,indent=4,sort_keys=True)

x.close()