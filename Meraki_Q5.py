import json

a='{ "Name":"David", "Class":"I", "Age":6}'

b=json.loads(a)

c={"a":12,"b":34,"c":45}

for i in c:
    b[i]=c[i]

print(b)