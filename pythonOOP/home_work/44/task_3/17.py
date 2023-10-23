# task 1        Беспятий Дмитро

# from random import randint, seed
# seed(1)
#
# n = 10
#
# list_1 = [randint(1, n) for _ in range(n)]
# list_2 = [randint(1, n) for _ in range(n)]
# print(list_1, list_2)
#
# list_3 = list_1.copy()
# list_3.extend(list_2)
# print(f'елементи обох списків: {list_3}')
#
# list_3_spil = []
# for i in list_1:
#     for j in list_2:
#         if i == j and i not in list_3_spil:
#             list_3_spil.append(i)
# print(f'елементи, спільні для двох списків: {list_3_spil}')
#
# list_3_unic_1 = [i for i in list_1 if list_1.count(i) == 1]
# list_3_unic_2 = [i for i in list_2 if list_2.count(i) == 1]
# list_3_unic = list_3_unic_1.copy()
# list_3_unic.extend(list_3_unic_2)
# print(f'унікальні числа списку 1, 2: {list_3_unic}')
# print(f'Максимальне число списку  1: {max(list_1)}, '
#       f'Мінімальне число списку  1: {min(list_1)}')
# print(f'Максимальне число списку  2: {max(list_2)}, '
#       f'Мінімальне число списку  2: {min(list_2)}')



#task 2        Беспятий Дмитро

# data = """ Om Bhakta male 26 Mar 1976 1707.0
# Krishnin Kakar male 18 Apr 2011 2482.33333
# Neela Tara female 27 Apr 1995 529.33333
# Ajit Pandya male 21 Aug 2001 1231.33333
# Kavita Goda female 25 Jan 1986 1281.33333
# Avinash Tata male 20 Sep 2004 2767.0
# Narinder Raval male 23 Dec 2019 2309.66667
# """
# import datetime
# lst = data.strip().split('\n')
# text = []
# full_name = ''
# full_name_1 = ''
# gender = ''
# age = ''
# age_1 = 0
# age_2 = ''
# age_3 = 0
# balance = 0
# char = ''
#
# for i in lst:
#       for j in i:
#             if j == ' ':
#                   text.append(char)
#                   char = ''
#             elif j == ',':
#                   break
#             else:
#                   char += j
#       text.append(char)
#       char = ''
#
# print('{full_name}|{gender}|{age}|balance'.\
#       format(full_name='full_name'.center(20,'*'), gender='gender'.center(10,'#'), age="age".center(5,"-")))
#
# n = 0
# for char in range(7):
#       for i in range(n, len(text)):
#             if i == n:
#                 full_name_1 = text[i]
#             else:
#                   break
#       for j in range(n+1, len(text)):
#             if j == n + 1:
#                   full_name += full_name_1 + ' ' + text[j].upper()
#             else:
#                   break
#       for k in range(n+2, len(text)):
#             if k == n + 2:
#                   gender = text[k].capitalize()
#             else:
#                   break
#       for q_1 in range(n+3, len(text)):
#             if q_1 == n + 3:
#                   age_1 = int(text[q_1])
#             else:
#                   break
#       for q_2 in range(n+4, len(text)):
#             if q_2 == n + 4:
#                   age_2 = text[q_2]
#                   if age_2 == 'Jan':
#                         age_2 = 1
#                   elif age_2 == 'Feb':
#                         age_2 = 2
#                   elif age_2 == 'Mar':
#                         age_2 = 3
#                   elif age_2 == 'Apr':
#                         age_2 = 4
#                   elif age_2 == 'May':
#                         age_2 = 5
#                   elif age_2 == 'Jun':
#                         age_2 = 6
#                   elif age_2 == 'Jul':
#                         age_2 = 7
#                   elif age_2 == 'Aug':
#                         age_2 = 8
#                   elif age_2 == 'Sep':
#                         age_2 = 9
#                   elif age_2 == 'Oct':
#                         age_2 = 10
#                   elif age_2 == 'Nov':
#                         age_2 = 11
#                   elif age_2 == 'Dec':
#                         age_2 = 12
#             else:
#                   break
#       for q in range(n+5, len(text)):
#             if q == n + 5:
#                   age_3 = int(text[q])
#                   date1 = datetime.date(year=age_3,month=age_2,day=age_1)
#                   d_today = datetime.date.today()
#                   are = (d_today - date1) / 365
#             else:
#                   break
#       for r in range(n+6, len(text)):
#             if r == n + 6:
#                   balance = text[r]
#             else:
#                   break
#       print('{:20} {:^10} {:^+5} {:.7}'.format(full_name, gender, are.days, balance))
#       full_name = ''
#       full_name_1 = ''
#       gender = ''
#       age = ''
#       balance = ''
#       n += 7