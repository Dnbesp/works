# task 1                Беспятий Дмитро

import json
import pickle
import csv
from csv import DictReader

# strng = """{
#     "emp1":{
#         "name":"Lisa",
#         "designation": "programmer",
#         "age": 34,
#         "salary": 54000
#     },
#     "emp2":{
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": 24,
#         "salary": 40000
#     }
# }"""
#
# obj = json.loads(strng)
# print(type(obj))
#
# for item in obj.items():
#     print(*item)
#
# obj['emp3'] = {'name': 'Eddi', 'designation': 'engen', 'age': 30, 'salary': 45000}
#
# # 1
# with open("strng2.json", mode='w') as file:
#     json.dump(obj, file, indent=4)
#
# # 2
# with open("strng3.pkl", mode='wb') as bin_file:
#     pickle.dump(obj, bin_file)
#
# # test (==)
# with open("strng2.json", mode='r') as file2:
#     js = json.load(file2)
#
# with open("strng3.pkl", mode='rb') as bin_file2:
#     pkl = pickle.load(bin_file2)
#
# print(js == pkl)

# task 2                Беспятий Дмитро

# def validate_json(js_str):
#     print(js_str)
#     try:
#         json.loads(js_str)
#         print("Valid JSON")
#     except ValueError:
#         print("Inalid JSON,", 'ValueError: JSONDecodeError')
#         return None
#
#
# validate_json('{"name": "Lisa", "designation": "programmer", "age": 34}')
# print()
# validate_json('"name", "Lisa", "designation", "programmer"')

# task 3                Беспятий Дмитро

# def covert_csv_to_json(cover_csv, cover_json):
#     with open('text.csv') as file, open("json.json", mode="w") as file_js:
#         try:
#             csv_tex = DictReader(file, delimiter=';')
#             csv_new = {}
#             for cs in csv_tex:
#                 key = cs['No']
#                 del cs['No']
#                 csv_new[key] = cs
#             json.dump(csv_new, file_js, indent=4)
#             result = "операція перетворення успішна"
#         except Exception:
#             result = "операція перетворення не успішна"
#     return result
#
# cover_csv, cover_json = "text.csv", "json.json"
#
# print(covert_csv_to_json(cover_csv, cover_json))
