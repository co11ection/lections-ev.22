# # # # # # name = 'lol'
# # # # # # # print(name) 
# # # # # # экронирование - механизм при помощи которого можно вставлять символы
# # # # # # которые сложно вести с клавиатуры
# # # # # from sys import set_coroutine_origin_tracking_depth


# # # # # \n -> perenos stroki 
# # # # # \t -> гориз табуляция
# # # # # \f -> перевод страницы
# # # # # \r -> возврат указателя (коретки)
# # # # # \v -> вертикальная табуляция

# # # # index in string

# # # name = 'John'
# # # print(name[0])
# # # print(name[-1])
# # ********************************************************************************************************
# # # срезы по индексам

# # import string
# # from tracemalloc import start


# # string[start: end: step:]
# # len()- vyvodit dlina stroki

# # text = 'hello world my name is john snow'
# # print(text[0:5])
# # print(text[10:-1])
# # print(text[10::2])
# # *******************************************************************************************************
# # конкатенация строк (слияние, соединение обьектов или строк)
# # word1 = 'hello'
# # word2 = 'world'
# # probel = ' '
# # result = word1 + probel + word2
# # print(result + ' !!')
# # print(len(result))
# # *****************************************************************************************************
# #  Форматирование строк
# # 1)  с помощью % 
# # 2) с помощью метода .format()
# # 3) Интерпoляция строк (f-строки)

# # %
# from unicodedata import name


# name = input('enyer your name: ')
# lastName = input('Enter your last name: ')
# print('hello, mr\ms %s %s' %(name, lastName))

# .format
# name = input('enyer your name: ')
# lastName = input('Enter your last name: ')
# print('hello mr\ms {} {}' .format(name, lastName))

# interpolasia (f-string)
# name = input('enyer your name: ')
# lastName = input('Enter your last name: ')
# print(f'hello mr\ms {name} {lastName}')

# print('h/w 3')
# string = 'timurlan'
# print(string[-1:-3: 1])

# foxAndDog = "The quick brown fox jumps over the lazy dog"
# # editedFoxAndDog = foxAndDog.replace('o','*')
# # print(editedFoxAndDog)

# name = 'timurlan'
# print(name[-1:] + name[1:-1] + name[:1] )


# import string
# import random
# from typing import List

# def generate_random_string(length: int, *choices: str) -> str:
#     """
#     Generate a string of a given `length`.

#     The result has at least one symbol from each of `choices` if `length` allows.

#     Arguments:
#         length -- Result string length.
#         choices -- Strings with available symbols.
#     """
#     if not choices:
#         # будем использовать только буквы если нам все равно, из каких символов пароль
#         choices = (string.ascii_letters, ) 

#     # создадим строку со всеми доступными символами
#     all_choices = "".join(choices)
#     result: List[str] = []
#     choice_index = 0
#     while len(result) < length:
#         # получим по символу из каждого списка, чтобы
#         # каждый список был использован хотя бы один раз
#         if choice_index < len(choices):
#             symbol = random.choice(choices[choice_index])
#             result.append(symbol)
#             choice_index += 1
#             continue

#         # а после этого добавляем символы из любого списка
#         symbol = random.choice(all_choices)
#         result.append(symbol)

#     # перемешаем наш результат чтобы распределить начальные символы
#     random.shuffle(result)
#     return "".join(result)


