#          0    1    2    3    4   5   6   7   8   9  10  11     sum =12
list_1 = [321, 123, 234, 345, 11, 22, 33, 44, 55, 66, 77, 88]

# print(len(list_1))
#
# for item in list_1:
#     print(item)

#                         12
# for index in range(1, len(list_1), 2):
#     print(list_1[index])

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6],
    [7, 8, 9, 10, 11]
]

# print(len(matrix))
# print(matrix[0])
# print(len(matrix[0]))
# print(len(matrix[1]))
# print(len(matrix[2]))


# for items in matrix:
#
#     for item in items:
#         print(item)


# user = dict(id=1, name='vasya', age=31)
#
# for key in user:
#     print(key, user[key], type(user[key]))

# list_1 = [321, 123, 234, 345, 11, 22, 33, 44, 55, 66, 77, 88]

# counter = 0
# while counter < len(list_1):
#     print(list_1[counter])
#     counter = counter + 1

sum = 0
for item in list_1:
    sum = sum + item

# print(sum)

# for item in reversed(list_1):
#     print(item)
#

counter = len(list_1) - 1
# print(counter)

# while counter >= 0:
#     print(list_1[counter])
#     counter = counter - 1


for item in list_1[::-1]:
    print(item)
