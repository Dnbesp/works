
# strg = "Python Ruby C++ C Java Go JavaScript".split()
# print(strg)
#
# # 1
# file = open("output.txt", mode="w")
# for row in strg:
#     file.write(f'{row}\n')
#     #file.write("\n")
# file.close()
#
# # 2
# strg_2 = [x + "\n" for x in strg]
# file = open("output2.txt", mode="w")
# file.writelines(strg_2)
# file.close()

# with open("output.txt", mode="r") as file:
#     print("pos=", file.tell())
#     text = file.read(3)
#     print("pos=", file.tell())
#     print(text)
#     file.seek(20)
#     text = file.read()
#     print(text)

# with open("output.txt", mode="r") as file:
#     lines = file.readlines()
#     print(lines)
#     file.seek(0)
#     for line in file:
#         print(line.rstrip())

# with open("output.txt", mode="r") as file:
#     lines = file.readlines()
#     print(lines)
#     file.seek(0)
#     for line in file:
#         print(line.rstrip())

from pprint import pprint
# with open("output.txt", mode="r") as file:
#     while True:
#         try:
#             line = next(file)
#             print(line.rstrip())
#         except StopIteration:
#             break
