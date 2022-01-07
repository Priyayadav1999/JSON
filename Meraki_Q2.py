
import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}

x=open("my_file1.json","w")

json.dump(a,x,indent=4)

x.close()