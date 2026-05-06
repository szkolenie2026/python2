import json

x =  '{ "name":"Rafał", "color":"black", "city":"Wwa"}'

y = json.loads(x)

print(y["color"])