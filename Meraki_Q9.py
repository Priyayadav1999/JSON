import json
a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

k=open("json_file.json","w")
json.dump(a,k, indent=4)
k.close()

x=open("json_file.json","r")
y=json.loads(x.read())

for i in y.values():
    item=input("enter the item you want to purchase=")
    quantity=int(input("enter the quantity="))
    for a,b in i.items():
        if item==a:
            remaining_quantity=int(b)-quantity
            i[a]=str(remaining_quantity)
d=open("json_file.json","w")
json.dump(y,d,indent=4)

d.close()
x.close()
