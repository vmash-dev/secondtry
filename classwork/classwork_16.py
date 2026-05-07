
# file = open('requirements.txt')
#
# content = file.read()
# print(content)
# file.seek(0)
# content = file.read()
# print(content)
# # 1/0
#
# file.close()
# content = file.read()
# ...


# open file
with open('requirements.txt', encoding='utf-8') as file:
    # # all rows
    # content = file.read()
    # print(content)

    # # all rows as list of strings
    # lines = file.readlines()
    # print(lines)
    # for line in lines:
    #     # '\n\n'
    #     print(line, end='')

    flag = True
    while flag:
        line = file.readline()
        print(line, end='')

        if 'tornado' in line:
            break
        if not line:
            # break
            flag = False