import json


json_data='{"a":1,"b":2,"c":3}'

loaded_json=json.loads(json_data)
print(loaded_json)
print("keys:values")
for key in loaded_json:
    print(key+":"+str(loaded_json[key]))

print(loaded_json['c'])
