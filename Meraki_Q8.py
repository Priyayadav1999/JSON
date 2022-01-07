import json
a=   [["neelam","programer","24","2400",],["komal","trainer","24","20000"],
     ["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"]]

new=["emp1", "emp2", "emp3", "emp4"]
new_list=["name","designation","age","salary"]

dict={}
for i in range(len(new)):
    dic1={}
    for j in range(len(a)):
        dic1[new_list[j]]=a[i][j]
    dict[new[i]]=dic1

b=open("json_dict.json","w")
json.dump(dict,b,indent=4)

b.close()
