import json
from os import read

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
# print(type(dict1))

out_file = open("myfile.json", "w")
  
json.dump(dict1, out_file, indent = 6)
# print(type(out_file))
  
out_file.close()

x=open("myfile.json","r")

print(x.read())

x.close()