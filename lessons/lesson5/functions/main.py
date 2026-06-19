from unittest import result

list_1 = [11, 22, 33, 44, 55]
list_2 = [111, 122, 133, 144, 155]
list_3 = [1111, 1212, 1313, 1414, 1155]


def printer(array):
    for item in array:
        print(item)
    print('==================')


# printer(list_1)
# printer(list_2)
# printer(list_3)


def printer(array, direction):
    if direction == 'asc':
        for item in array:
            print(item)
    elif direction == 'desc':
        for item in reversed(array):
            print(item)


# printer(list_1, 'desc')


def calculator(a, b):
    result = a + b
    return result


x = calculator(10, 20)

sum = 100 + x
print(sum)


def calculator(a, b, action):
    match action:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            return 'Error'


xxx = calculator(10, 20, '-')
print(xxx)


def foobar(param, param1, param2):
    resuk = param + param1 + param2
    print(resuk)
    return resuk


x = foobar(10, 20, 30)


