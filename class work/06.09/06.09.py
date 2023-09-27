json_str= """[
 {
  "Employee ID": 1,
  "Name": "Abhishek",
  "Designation": "Software Engineer"
 },
 {
  "Employee ID": 2,
  "Name": "Garima",
  "Designation": "Email Marketing Specialist"
 }
]"""
# Запишіть вмістиме json_str у json-файл
# Завантажте отриманий json-файл та перетворіть дані у  файл CSV.


# 1
import json
#
# try:
#     json.loads(json_str)
# except json.JSONDecodeError:
#     print("Incorect json-str")
# else:
#     try:
#         with open("sample1.json", mode='w') as file:
#             file.write(json_str)
#     except FileExistsError:
#         print("File exists")

# 2
#
# with open("sample2.json", mode='w') as file:
#     try:
#         lst = json.loads(json_str)
#         json.dump(lst,file, indent=4)
#     except json.JSONDecodeError:
#         print("Incorect json-str")

# 3
# import csv
# with open("sample2.json") as json_f, open("sample.csv", mode='w') as csv_f:
#     lst = json.load(json_f)
#     print(lst)
#     writer = csv.DictWriter(csv_f, fieldnames=lst[0].keys(), lineterminator='')
#     writer.writeheader()
#     for item in lst:
#         print(item)
#         writer.writerow(item)






