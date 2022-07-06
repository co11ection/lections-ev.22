# """. Сгенерируйте рандомный пароль
#  который будет следовать следующим
#   требованиям: пароль должен
#    содержать 2 символа верхнего регистра, 
#    одно число и один спец.символ.
#     Подсказка: Используйте библиотеки random и string.
# """
# import random
# import string
# letter1 = random.choice(string.ascii_uppercase)
# letter2 = random.choice(string.ascii_uppercase)
# number = random.randint(1,10)
# simbol = random.choice(string.punctuation)
# password = [letter1,letter2,str(number),simbol]
# random.shuffle(password)
# password = ''.join(password)
# print(password)