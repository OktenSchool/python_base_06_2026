recips = [123, 234, 345, 456]
recips.append(100500)

print(recips)

usersNames = ['vasya']
usersNames.append('petya')
usersNames.append('max')

print(usersNames)

# usersNames.remove('petya')
# print(usersNames)

#                  0        1        2
# usersNames =  ['vasya', 'petya', 'max']
print(usersNames[0])
print(usersNames[1])
print(usersNames[2])

# user1Properies = [38, 'serj', True]

user1 = dict(age=38, name='serj', isMarried=True)
print(user1)
print(user1['age'])
print(user1['name'])

user2 = {
    "name": "petya",
    "age": 38,
    "is_married": True,
    # "wife": dict(name='anna', age=29)
    "wife": {"name": "anna", "age": 29},
    "wallet": [10, 10, 20]
}

print(user2)

print(user2['wife']['name'])
print(user2['wallet'][2])

users = [
    user1,
    user2,
    dict(name='kokos', age=123),
    {"name": 'abrikos', "age": 234}
]

print(users)
users.append(dict(name='oak', age=987))
print(users)

# tuples
# nums = (1, 2, 3)
# print(nums)

set_1 = {11, 11, 22, 11, 33, 44, 567}
print(set_1)

set_2 = {'asd', 'qwe', 'asd'}
print(set_2)
