import json

a =  '{ "Name":"David", "Class":"I", "Age":6 }'

b=json.loads(a)
print(b)
print(type(b))