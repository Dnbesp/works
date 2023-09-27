# task 1                Беспятий Дмитро

# import sys
#
# strg = '''Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:'''
#
# with open('new_file.txt', mode='w') as file:
#         file.write(strg)
#
# print(sys.argv)
#
# def write_file():
#     with open('new_file.txt') as file2, open('file_2_2.txt', mode='w') as file3:
#         read_fil = file2.readlines()
#         for item in read_fil:
#             k = item[0]
#             w = item[1]
#             item = ''.join(item)
#             item = item.replace(item[1], k, 1)
#             item = item.replace(item[0], w, 1)
#             file3.write(item)
# write_file

# task 2                Беспятий Дмитро

# strg = '''In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer'''
#
# with open('file_2.txt', mode='w') as file:
#     file.write(strg)
#
# # 1
# with open('file_2.txt') as file2, open('file_2_2.txt', mode='w') as file3:
#     read_fil = file2.read()
#     file3.write(read_fil)
#
# # 2
# with open('file_2_2.txt') as file4, open('file_2_3.txt', mode='w') as file5:
#     read_fil2 = file4.readlines()
#     for item in read_fil2:
#         item = item.split().__reversed__()
#         item = ' '.join(item)
#         file5.write(f'{item}\n')

# task 3                Беспятий Дмитро

# with open('input.txt') as f, open('output_3.txt', mode='w') as f_2:
#     line = f.read()
#     line = list(line)
#     sum = 0
#     for i in line:
#         if i.isdigit():
#             sum += int(i)
#     f_2.write(f'{sum}')

# task 4                Беспятий Дмитро

with open('input_4.txt') as f, open('output_4', mode='w') as f_2:
    line = f.readlines()

    for l in line:
        l = l.split()
        sum_num = sum(int(i) for i in l[2::])/len(l[2::])
        if sum_num > 6:
            f_2.write(f'{l[0]}\n')
