import json

x = """{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""

# print(x, type(x))
obj = json.loads(x) # from json-str get dict-obj
obj["salary"] = 2000
# print(type(obj))
# print(obj["Hobbies"][1])
# for k, v in obj.items():
#     print(f'{k=},{v=}')
print(obj)
# dict-obj --> sample.json
#1 method
with open("sampl.json", mode="w") as file:
    json.dump(obj, file, indent=4)

#2 method
with open("sampl2.json", mode="w") as outfile:
    json_str = json.dumps(obj) # dict-obj get from json-str
    print(f'{json_str=}')
    outfile.write(json_str)

# Бінарна серилізація
import pickle
with open("sample3.pkl", mode="wb") as bin_file:
    pickle.dump(obj, bin_file)







