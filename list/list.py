# list() -> (список, массив) - изменяемыый, последовательный тип данных который из себя представляет коллекцию каких-либо обьектов

# myList = [1, 'string', False, None, [1,2,3]]
# print(myList)
# print(type(myList))
# *********************************************************************************************************************
# 1) --> list(<interable>)
# list = list('hello world')
# print(list)

# tuple_ = ('banana', 'apple', 'chery')
# print(tuple_)
# list = list(tuple_)
# print(list)

# 2) --> range() ->  возвращает послед элементо(чисел)
# a = list(range(1,15, 2))
# print(a)

# 3) --> []
# list = []
# print(list)
# ********************************************************************************************************************

                                  # list methods
# 1) append(elements) -  добовляет элемент в конец списка

# list_ = [1,2,3]
# print(list_)
# list_.append(5)
# list_.append([1,2,3])
# print(list_)

# 2)extend(element[iterable]) --> рассширяет список добовляя элемент в конец. 
# list_ =[1,2,3]
# list_.extend([1,2,3])
# print(list_)


# 3) insert(<index>, <element>) -> добовляет элемент по указанному индексу
# list_ = ['string', 1, 3, False]
# list_.insert(2,[1,2,None])
# list_.insert(1,3)
# print(list_)

# ******************************************************************************************************************

# index(element, [start], [end])-  возвращает индекс элемента

# ls = [1,2,3,33,3,4,5,5,3,4,4, 'hello']
# print(ls.index)
# if 'hello' in ls:
#     print(f'"hello " is in list {ls.index("hello")}')
# ******************************************************************************************************************


# count(element) -->  возвращает колличество вхождений element в списки

# ls = [1,2,3,4,4,4,5,1]
# result = ls.count(4)
# print(result)

# *****************************************************************************************************************

# remove(element) - ->  удаляет элемент. если такого лемента нет в списке то выводит ошибку
# pop([index])-удаляет и возвращает элемент по индексу, но если индекс не указан то удаляет последний элемен

# ls = [1,2,3,4,4,4,5,1]
# ls.remove(4)
# ls.remove(4)
# print(ls)
# ls.pop()
# print(ls)

# **********************************************************************************************************************************************************

# sort([revers= True/False], [keys=<>]) --> сортировка списка, если в аргументе указан reverse = True то список будет отсортирован в убыв порядке

# ls = [5,3,4,3,0,-2,10,102,2]
# ls.sort(reverse = False)
# print(ls)

# ls = ['hello', ' john', 'London']
# ls.sort()
# print(ls)
# ls.sort(reverse=True, key=len)
# print(ls)



# zamena and izmenenie
# ls = [1,2,3,'h']
# ls [3] = 4
# print(ls)



# ls = [1,2,3,'h']
# ls [3] = 4
# del ls[-1]
# print(ls)
# print(dir(tuple))

