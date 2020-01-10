import json

#--- STRING TO JSON - LOADS ---#
jsonstr = '{"name": "Max", "email": "max@abc.com"}'
jsonobj = json.loads(jsonstr)

print(jsonobj)
print(jsonobj["email"])

#--- JSON TO STRING - DUMPS ---#
jsonobj = {
    "age": 17,
    "role": "designer",
    "depts": ["Dept. A", "Dept. C"],
    "values": [
        {"phone": "123456"},
        {"email": "abc@xyz"}
    ]
}

jsonstr = json.dumps(jsonobj)

print(jsonstr)
