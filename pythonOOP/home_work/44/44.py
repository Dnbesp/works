# task 1                    Беспятий Дмитро

#   Напишіть функцію, яка виводить розмір кожного файлу в заданому  каталозі, його значення в байтах, дату/час
#   створення та зміни. Якщо каталога із вказаним ім’ям немає, генерується виняток. Використайте модулі os і time.

import os
import time
import shutil
from pathlib import Path
from os.path import join, getsize


# def size(direct):
#     try:
#         for filenames in os.scandir(direct):
#             os_file = os.stat(filenames)
#             print(f'{os.fsdecode(filenames)}, size file: {os_file.st_size} bytes, data creation: {time.ctime(os_file.st_ctime)}, '
#                   f'data changes: {time.ctime(os_file.st_mtime)}')
#     except FileNotFoundError:
#         print(f'введеного шляху не існує')
#
#
# size_direc = size("dir")


# task 2                    Беспятий Дмитро

# Функція приймає розширення файлів, директорію-1 і директорію-2, і  робить резервну копію усіх файлів із цими
# розширеннями із директорії-1 у директорію 2. Можна скористатись `shutil.copy2()`.

# def copy(type_file, direct_1, direct_2):
#     for file in os.scandir(direct_1):
#         tf = Path(file).suffix == type_file
#         print(tf)
#         if tf:
#             shutil.copy2(file, direct_2)
#
#
# c = copy('.py', 'data_1', 'data_2')


# task 3                    Беспятий Дмитро

# Розрахувати загальний розмір та кількість усіх файлів у заданій директорії та її піддиректоріях.
# Використати функцію os.walk()

# def size(direct):
#     count = 0
#     sum_size = 0
#     for root, dirs, files in os.walk(direct):
#         for file_name in files:
#             sum_size += getsize(join(root, file_name))
#             count += 1
#
#     print(f'Загальний розмір файлів в директорії "{direct}" = {sum_size} bytes, '
#           f'кількість файлів = {count}')
#
#
# direc = size('task_3')
