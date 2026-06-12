# age = 10
# control_age = 18
#
# if age >= control_age:
#     print(f'good your age is {age} greater than {control_age}')
#
# else:
#     print(f'bad your age is {age} less than {control_age}')
from unittest import case

# age = 61
# control_age_1 = 18
# control_age_2 = 60
#
# if age < control_age_1:
#     print('cheap phones')
# elif age >= control_age_1 and age < control_age_2:  # 18-59
#     print('premium phones')
# elif age >= control_age_2:
#     print('grandma phones')
#
# else:
#     print('no phones')


# age = 59
# control_age_1 = 18
# control_age_2 = 60
#
#  if age < control_age_1:
#     print('cheap phones')
# elif age >= control_age_1:
#     if age < control_age_2:
#         print('premium phones')
#     else:
#         print('cool phones')
# else:
#     print('asgdjsahgd')


language = 'en'

match language:
    case 'en':
        print('hello')
    case 'uk':
        print('Привіт')
    case 'es':
        print('Hola')
    case _:
        print('i dont understand you sorry michael')
