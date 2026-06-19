user = dict(id=1, name='vasya')

print(user)
print(user.get('id'))
print(user.keys())
print(user.values())
user.clear()
print(user)

list = [11, 22, 33, 44, 11, 33, 22, 11]

print(list.count(11))
list.insert(0, 10500)
print(list)

list.reverse()
print(list)

list.sort(reverse=True)
print(list)
