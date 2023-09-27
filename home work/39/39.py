# task 1                Беспятий Дмитро

# strg_1 = 'In the above example you may notice a keen difference in the parameters of the inner function'.split()
# strg_2 = 'In makes it a general may that can decorate a function having any number of arguments'.split()
#
# file = open("output.txt", mode="w")
# for row in strg_1:
#     file.write(f'{row}\n')
# file.close()
#
# file = open("output2.txt", mode="w")
# for row in strg_2:
#     file.write(f'{row}\n')
# file.close()
#
# with open("output.txt", mode="r") as file, open("output2.txt", mode="r") as file2:
#     try:
#         line = file.readlines()
#         line2 = file2.readlines()
#         for i in range(len(line)):
#             if line[i] != line2[i]:
#                 print(f'{line[i].rstrip(), line2[i].rstrip()}')
#             else:
#                 continue
#     except IndexError:
#         print("Всі строки текстових документів порівняні між собою")

# task 2                Беспятий Дмитро

# strg = """1. Python is an easy to learn, powerful programming language.
# 2. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
# 3. Python’s elegant syntax and dynamic typing, together with its interpreted nature,
# make it an ideal language for scripting and rapid application development in many areas on most platforms.
#
# 4. The Python 3 interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web
# site.
# 5. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
# """
#
#
# with open('language.txt', mode='w') as file:
#     file.write(strg)
#
# with open('output_2.txt', mode='w') as file, open('language.txt') as file2:
#     text = file2.read()
#     file2.seek(0)
#     lines = file2.readlines()
#
#     # 1
#     ascii = list(map(lambda item: item.isascii(), text))
#     len_ascii = len(list(filter(lambda item: item == True, ascii)))
#     file.write(f'Кількість символів "ASCII": {len_ascii}\n')
#
#     2
#     file.write(f'Кількість рядків: {len(lines)}\n')
#
#     # 3
#     items_gol = ['a', 'e', 'i', 'o', 'u', 'y']
#     gol = list(map(lambda item: item.lower() in items_gol, text))
#     len_gol = len(list(filter(lambda item: item == True, gol)))
#     file.write(f'Кількість голосних букв: {len_gol}\n')
#
#     # 4
#     items = [",", ".", "-", "’", "!", "?"]
#     asc = list(map(lambda item: item in items, text))
#     len_asc = len(list(filter(lambda item: item == True, asc)))
#     file.write(f'Кількість знаків пунктуації: {len_asc}\n')
#
#     # 5
#     digit = list(map(lambda item: item.isdigit(), text))
#     len_digit = len(list(filter(lambda item: item == True, digit)))
#     file.write(f'Кількість цифр: {len_digit}\n')
#
#     # 6
#     l = 0
#     count = 0
#     num = 0
#     for item in lines:
#         count += 1
#         if len(item) > l:
#             l = len(item)
#             num = count
#
#     file.write(f"Довжина найдовшого рядка: {l}, номер рядка: {num}\n")
#
#     # 7
#     text2 = text.split()
#     python = list(map(lambda item: item == 'Python', text2))
#     len_python = len(list(filter(lambda item: item == True, python)))
#     file.write(f'Кількість слів "Python": {len_python}\n')

# task 3                Беспятий Дмитро

# with open('language.txt') as file, open('output_3.txt', mode="w") as file2:
#     lines = file.readlines()
#
#     del lines[-1]
#     for i in range(len(lines)-1):
#         if len(lines[i]) == 1:
#             del lines[i]
#
#     lines[1], lines[2] = lines[2], lines[1]
#
#     file2.writelines(lines)

# task 4                Беспятий Дмитро

stock_prices = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42,
200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]

with open('list.txt', mode='w') as file:

    stock = ' '.join(str(e) for e in stock_prices)
    stock = stock.split()
    file.write("\n".join(stock))
    file.write('\n')

    stock.sort()
    file.write(" ".join(stock))

