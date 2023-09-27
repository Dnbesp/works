# task 1                Беспятий Дмитро
# 1
import csv
import json
import requests

# def site(http, name_csv):
#     try:
#         with open(name_csv, 'w', newline='') as file:
#             text = requests.get(http)
#             csv_file = text.text.replace(';', ',')
#             file.write(csv_file)
#             result = "Операція успішна"
#     except requests.exceptions.MissingSchema:
#         result = "Невірно вказаний URL сторінки, операція не успішна"
#     except FileNotFoundError:
#         result = "Невірно вказана назва csv файлу, операція не успішна"
#     return result
#
#
# inf_site = site("https://support.staffbase.com/hc/en-us/article_attachments/"
#                 "360009197091/email-password-recovery-code.csv", 'new.csv')
#
# print(inf_site)

# 2

# def change_csv_value(file_path, row_index, column_name, new_value):
#
#     """Функція для зміни будь-яких рядків і стовпців, на вказане значення"""
#
#     try:
#         with open(file_path) as file, open(file_path, 'r+') as file2:
#             file_csv = csv.DictReader(file)
#             fieldnames = ['Login email', 'Identifier', 'One-time password', 'Recovery code',
#                           'First name', 'Last name', 'Department', 'Location']
#             file_csv2 = csv.DictWriter(file2, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
#             file_csv2.writeheader()
#             count = 0
#             for item in file_csv:
#                 if column_name not in item:
#                     result = 'Операція прошла не успішно, невірно введена назва рядку'
#                     break
#                 else:
#                     if count == row_index:
#                         item[column_name] = new_value
#                     file_csv2.writerow(item)
#                     count += 1
#                     result = 'Операція прошла успішно'
#             if row_index > count:
#                 result = 'Операція прошла не успішно, введений індекс більше ніж max в файлі'
#     except (TypeError, SyntaxError):
#         result = "Введіні невірні данні для змін"
#     except (FileNotFoundError, UnboundLocalError):
#         result = "Введено некоректне місцезнаходження файлу CSV"
#
#     return result
#
#
# change_inf = change_csv_value('C:\\Users\\UABDMB_adm\\PycharmProjects\\home work\\43\\new.csv', 0,
#                           'Login email', 'email@com.ua')
#
# print(change_inf)

# 3

# def change_password(email, new_value, file_path):
#
#     """Функція для зміни одноразового параля користувача за email"""
#
#     try:
#         with open(file_path) as file, open(file_path, 'r+') as file2:
#             file_csv = csv.DictReader(file)
#             fieldnames = ['Login email', 'Identifier', 'One-time password', 'Recovery code',
#                           'First name', 'Last name', 'Department', 'Location']
#             file_csv2 = csv.DictWriter(file2, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
#             file_csv2.writeheader()
#             count = 0
#             for item in file_csv:
#                 if item['Login email'] == email:
#                     item['One-time password'] = new_value
#                     count += 1
#                     result = 'Операція прошла успішно'
#                 file_csv2.writerow(item)
#             if count == 0:
#                 result = 'Операція прошла не успішно, введений email відсутній у файлі'
#     except (TypeError, SyntaxError):
#         result = "Введіні невірні данні для змін"
#     except (FileNotFoundError, UnboundLocalError):
#         result = "Введено некоректне місцезнаходження файлу CSV"
#
#     return result
#
#
# change_pas = change_password('laura@example.com', '11ww11',
#                          'C:\\Users\\UABDMB_adm\\PycharmProjects\\home work\\43\\new.csv')
#
# print(change_pas)

# 4

# def del_user(email, file_path):
#
#     """Функція для видалення користувача за заданим email"""
#
#     try:
#         with open(file_path) as file:
#             file_csv = csv.DictReader(file)
#             file_csv_list = list(file_csv)
#
#         with open(file_path, 'w') as file2:
#
#             fieldnames = file_csv_list[0].keys()
#             file_csv2 = csv.DictWriter(file2, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
#             file_csv2.writeheader()
#             count = 0
#             for item in file_csv_list:
#                 if item['Login email'] == email:
#                     count += 1
#                     result = 'Операція прошла успішно'
#                     continue
#                 file_csv2.writerow(item)
#             if count == 0:
#                 result = 'Операція прошла не успішно, введений email відсутній у файлі'
#     except (TypeError, SyntaxError):
#         result = "Введіні невірні данні для змін"
#     except (FileNotFoundError, UnboundLocalError):
#         result = "Введено некоректне місцезнаходження файлу CSV"
#
#     return result
#
#
# del_u = del_user('laura@example.com', 'C:\\Users\\UABDMB_adm\\PycharmProjects\\home work\\43\\new.csv')
#
# print(del_u)


# task 2                Беспятий Дмитро

def proekt(fn):

    """Реєстрація та аутентифікація користувача зі збереженням даних у файл json"""

    if fn == 'reg' or fn == 'log':
        try:
            name = input('Enter name: ')
            email = input('Enter email: ')
            pas = input('Enter password: ')
            inf_user = {'name': name, 'email': email, 'pas': pas}
            if fn == 'reg':

                with open('inf.json') as file:
                    js_inf = json.load(file)

                with open('inf.json', 'w') as file2:
                    count = 0
                    for item in js_inf:
                        if item['email'] == email:
                            count += 1
                            json.dump(js_inf, file2, indent=4)
                            result = 'Даний користувач вже зареєстрований'
                            break
                    if count == 0:
                        js_inf.append(inf_user)
                        json.dump(js_inf, file2, indent=4)
                        result = 'Реєстрація користувача виконана'
            if fn == 'log':

                with open('inf.json') as file_log:
                    js_inf_log = json.load(file_log)
                    for item in js_inf_log:
                        if item['email'] == email and item['pas'] == pas:
                            print("Вхід успішний")
                            chus = input("Enter chang, del or exit: ")
                            if chus == 'chang':
                                with open('inf.json', 'w') as file_chang:
                                    chan = input("Enter what need to changes(pas or email): ")
                                    if chan == 'pas':
                                        new_pas = input('Enter new password: ')
                                        for item in js_inf_log:
                                            if item['pas'] == pas:
                                                item['pas'] = new_pas
                                                json.dump(js_inf_log, file_chang, indent=4)
                                                result = 'Успішна зміна пароля'
                                                break
                                        break
                                    if chan == 'email':
                                        new_email = input('Enter new email: ')
                                        for item in js_inf_log:
                                            if item['email'] == email:
                                                item['email'] = new_email
                                                json.dump(js_inf_log, file_chang, indent=4)
                                                result = 'Успішна зміна email'
                                                break
                                        break
                                    else:
                                        json.dump(js_inf_log, file_chang, indent=4)
                                        raise UnboundLocalError
                            if chus == 'del':
                                with open('inf.json', 'w') as file_del:
                                    js_user = []
                                    for item in js_inf_log:
                                        if item['email'] == email:
                                            item.pop('name')
                                            item.pop('email')
                                            item.pop('pas')
                                            continue
                                        js_user.append(item)
                                    json.dump(js_user, file_del, indent=4)
                                    result = 'Обліковий запис видалено'
                            if chus == 'exit':
                                result = 'exit'
                                break
                            else:
                                raise UnboundLocalError
                        else:
                            raise UnboundLocalError
            if name == '' and email == '' and pas == '':
                raise UnboundLocalError
        except FileNotFoundError:
            with open('inf.json', 'a') as file_0:
                js_user = []
                js_user.append(inf_user)
                json.dump(js_user, file_0, indent=4)
            result = 'Перший користувач зареєстрований'
        except ValueError:
            result = 'Невірні значення'
        except UnboundLocalError:
            result = 'Помилка, невірний вибір'
    else:
        result = 'Введена функція не передбачена умовами програми'
    return result


inf = proekt(input('Enter function(reg or log): '))

print(inf)