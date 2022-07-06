# def <name_of_function>(<a,b>'#параметры'):
#     <body> # code, logic
#     <return# возвращаем что-то>

# <name_of_function(<a,b>'argumets')>

# parametrs - peremennye kotorye budut prinimat nasha func for that we can work with date which peredaiutsia into the func
# arguments - данные которые передаем для параметров при вызове функции




# def sumTwoNums(num1,num2):#parametrs
#     result = num1 + num2
#     print(result)
#     # return result
# sumTwoNums(5 , 5)
# # print(sumTwoNums(5 , 5)) #arguments



# def isEven(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# print(isEven(7))


# def isEven1(num: int) -> bool:
#     '''наша функция проверяет является ли число четным'''
#     if num%2==0:
#         return True
#     return False
# print(isEven1(5))



# def get_polindrom(words: list) -> list:
#     '''funcs return isPolindrom'''
#     result=[]
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result
# some_words = ['john', 'tenet']
# print(get_polindrom(some_words))


# default params

# def print_welcome(name: str = 'user')->str:
#     print(f'welcome { name}')
# print_welcome()




# def get_persent(money:float, year:int) ->float:
#     '''return final amount of money'''
#     if money<30000:
#         raise Exception ('min 30000')
#     if year <3:
#         raise Exception('you enter incorrect year for dipozit, min period year 3 years')
#     i =0
#     while i < year:
#         money = money+(money*0.1)
#         i+=1
#     return money
# money = float(input('Enter money '))
# year = int(input('Enter money '))
# print(get_persent(money, year))

'Hello world! My name is John, lata name is Snow! nice to meet you!'



# def get_revers(string1:str)->str:
#     list = string1.split(' ')
#     result1 = ' '.join(list[::-1])
#     print(result1)
#     return result1
# get_revers( 'Hello world! My name is John, lata name is Snow! nice to meet you!')






# num = int(input())
# string = str(num)
# list = list(string)

# print(sum([int(c) for c in list]))


# from csv import list_dialects


# def getDigitsSum(num:int)->int:
  
#   string = str(num)
#   list_ = list(string)
#   sum_ = sum([int(c) for c in list_]) 
#   return sum_ 

# num =int(input())
# print(getDigitsSum(num))


# def get_polindrom(words):
#   result=[]
#   for word in words:
#     if word.lower() == word[::-1].lower():
#       result.append(word)
#   return result
# some_words = ["кок", "топот", "комок"]
# print(get_polindrom(some_words))

# def walks(string):
#     res = False
#     x, y = 0, 0
#     if len(string) == 10:
#         for i in string:
#             if i == 'С': y += 1
#             if i == 'В': x += 1
#             if i == 'Ю': y -= 1
#             if i == 'З': x -= 1
#         res = True if x + y == 0 else False
#     return res
# print(walks(['С', 'В', 'В', 'В', 'Ю', 'Ю', 'З', 'З', 'З', 'С']))


def walks(naprav):
    res = False
    x, y = 0, 0
    if len(naprav) == 10:
        for i in naprav:
            if i == 'С': y += 1
            if i == 'В': x += 1
            if i == 'Ю': y -= 1
            if i == 'З': x -= 1
        res = True if x + y == 0 else False
    return res
dannye = ['С', 'Ю','В','З']
import random
naprav= []
list=[]
for i in range (10):
    list.append(i)
for i in list:
  naprav.append(random.choice(dannye))
print(naprav)
print(walks(naprav))