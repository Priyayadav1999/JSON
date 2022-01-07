import json

a=open("Text.txt","w")
a.write("Name Abhishek\n")
a.write( "Designation CEO of navgurukul\n")
a.write("Gender male\n")
a.write("Age 29")

a.close()

b="Text.txt"
dict={}

with open(b) as file:
    for x in file:
        key,desc=x.strip().split(None,1)
        dict[key]=desc.strip()

json_file=open("priya.json","w")
json.dump(dict,json_file,indent=4)

json_file.close()
