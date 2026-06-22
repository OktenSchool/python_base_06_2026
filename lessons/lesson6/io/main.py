# with open("xxx.txt", 'r', encoding="utf-8") as f:
#     # content = f.read()
#     # print(content)
#     for line in f:
#         print(line)


with open('xxx.txt', 'a', encoding='utf-8') as f:
    f.write('hello world1 \n')
    f.write('hello world2 \n')
