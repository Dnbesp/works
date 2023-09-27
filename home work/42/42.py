# task 1                Беспятий Дмитро
import csv
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
json_text = response.text

text = json.loads(json_text)

# 1
# count = 0
# id = ''
# userId = []
# num = 0
# for item in text:
#     if item["completed"] == True:
#         if count == 0 or count == 1:
#             id = item["userId"]
#             count += 1
#         else:
#             if item["userId"] != id and num < count:
#                 num = count
#                 userId.clear()
#                 userId.append(id)
#                 count = 1
#             elif item["userId"] != id and num > count:
#                 count = 1
#             elif item["userId"] != id and num == count:
#                 userId.append(id)
#                 count = 1
#             else:
#                 count += 1
# if num < count:
#     userId.clear()
#     userId.append(id)
# if num == count:
#     userId.append(id)
#
# print(f"Найбільше завдань виконав користувач: {userId}")
#
# # 2
# with open("data.json", mode='w') as file_js:
#     text2 = []
#     for item in text:
#         if item['completed'] == False:
#             text2.append(item)
#     json.dump(text2, file_js, indent=4)
#
# # 3
# with open('data.json') as file:
#     text3 = json.load(file)
#     print(list(filter(lambda item: (item['id'] > 100), text3)))

# task 2                Беспятий Дмитро

# 1
# with open('text_csv.csv', mode='w') as file_csv:
#     write = csv.DictWriter(file_csv, fieldnames=text[0].keys(), lineterminator='\n')
#     write.writeheader()
#     for item in text:
#         write.writerow(item)
#
# # 2
# def write_to_csv(userId, id, title, completed=False):
#     with open('text_csv.csv', 'a', newline='') as file_csv:
#         write = csv.writer(file_csv)
#         write.writerow([userId, id, title, completed])
#
# write_to_csv(11, 225, 'I need to do')