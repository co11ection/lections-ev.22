# # # # типы данных в коде 

# # # from types import NoneType
# # # from xmlrpc.client import Boolean


# # # 1. NoneTypes -> ничего, пустота
# # # 2. Boolean -> true/false
# # # 3. числовые типы данных:
# # # a) intger(int) -> целое число(1б2)
# # # b) float() -> чило с плав точкой(1.2, 2.7)
# # # с) complex() комплексный числа(3+5i/j)
# # # 4. списковые типы данных:
# # # a) list(список)(массив) -> [1,2,3, True, False, None,'hello world']
# # # b) tuple(кортеж) - > (1,2,3,False)
# # # 3) range(1,3) -> range(1,2)
# # # 5. str() -> string: "hello world", 'tima'
# # # 6. set() -> множества
# # # 7. dict -> словарь содержит данные в виде ключа : значения -> {1:'one', 2:'two'....}
# # # *************************************************************************************************


# # # Mutable(изменяемы типы данных)
# # # 1) list()
# # # 2) set()
# # # 3) dict()

# # # Imumtable (не изменяемые типы даннных)
# # # 1. NoneType
# # # 2. Boolean
# # # 3. int(), float(), complex()
# # # 4. str()
# # # 5. range()
# # # 6. tuple()
# # # ************************************************************************************************

# # '''стандвртный вывод данных'''
# # """в пайтоне для вывода данных используется функция  print()"""



# # print('hello world')
# # """Стандартный ввод данных через термиал  используется  input"""
# # a = int(input('введите чило:'))
# # # type()  выводит типы данных
# # print(a,type(a))
# # b = int(input('введите 2 число: '))
# # print(b, type(b))
# # print(a+b, a-b, a*b, a/b)

# # a = 1
# # b = -2
# # c = 3
# # print(pow(a, b,c))
# # print(divmod(23,1)) 
# # "выводит целечисленное деление a на b //,  а второе значение выводит остаток"
# # print(a//b)
# # abs()- "выводит обсолютное значение числа"
# # print(abs(a))
# # print(abs(b))

# # import math
# # a=5
# # print(math.sqrt(a))
# # a=15
# # print(int(a))
# # # //////////////////////
# # b='lol'
# # print(str(b))
# # # ///////////////////
# # x=3
# # y='lol '
# # print(y*x)
# # # ////////////////////////////
# # a = 4
# # b = -5
# # print(abs(a), abs(b))
# # # /////////////////////////////
# # a = 5
# # print(pow(a,2,5))
# # # //////////////////////////
# # x = int(input())
# # y = int(input())
# # z = 2.3
# # print(x%y*z)

# # import math
# # # d = 16
# # # print(pow(d,2), pow(d,3), math.sqrt(d))
# # import math
# # a = 3
# # b = 4
# # print(math.sqrt(pow(a,2)*pow(b,2)))
# # from cmath import pi
# # import math
# # r = int(input())
# # print(pi*pow(r,2))
# # x =3
# # y =4
# # z = 8
# # print(x, y, z)
# # x,z,y = y,x,z

# # print(x, z, y)
# # a =5
# # b =10
# # print(a, b)
# # c = a
# # a = b
# # b = c
# # print(a, b)

# # import random

# # x=random.uniform(0.1,  1)
# # y=random.uniform(9.5,  99.5)
# # print(x*y)

# 11001101000101000