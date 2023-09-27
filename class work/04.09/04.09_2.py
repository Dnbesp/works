import pickle, json
with open("sample3.pkl", mode="rb") as file:
    d = pickle.load(file)

print(type(d))

with open("sample.json", mode='r') as file:
    d_2 = json.load(file)

print(type(d_2))