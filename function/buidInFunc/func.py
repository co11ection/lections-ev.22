# встроенные функции
# map()
# filter()
# lambda
# enumerate()

# аноннимные фуникции - lambda(такие же функции только без названия) 
# lambda функции могут в себя принимать сколько угодно функциии но возвращвет только одно выражение


# def sums_args(a,b):
#     res = a+b
#     return res
# def sums_arg(a,b): return a+b

# print(sums_args(1,2))


# x = lambda a,b,c: a+b+c
# print(x(5,4,3))



# def func(n):
#     return lambda a: a*n
# doubler = func(2)
# print(doubler(22))

# ____________________________________________

# map(Function, iterable) -> приминяет  func  к каждом элементу последовательности и аозвращает mapobject(итератор) c результатами
#  Hапример с помощья map можно выпонять преоброзование элементов, все строки в верхнй регистр

# ls = ['one', 'two', 'three','dict']
# res = list(map(str.upper, ls))
# print(res)
# res2 = list(map(len, ls))
# print(res2)


# ls1 = ['1','2','3','4']
# res3 = list(map(int, ls1))
# print(res3)


# names = ['john', 'jame', 'sasha','tiron']
# res = list(map(lambda x: f'Hello mr\mrs {x}', names))
# print(res)



# nums =[1,2,3,4,5]
# num = [100,200,300,400,500]
# res = list(map(lambda x,y: x*y, nums,num))
# print(res)


# dict_  = {1:2, 3:4, 5:6}
# res = dict(map(lambda items:(items[0],str(items[1])),dict_.items()))
# print(res)
#-----------------------------------------------------------------------

# filter(function, Iterable) ->приминяет  func  ко вем элемента iteerable func  которую мы передаем 
# и возврщает filterobject(итератор) с теми обьектами для которых  func  вернуда true

# list_of_strings = ['one', 'two', 'list', 'John99', '50', '1','100']
# res = list(filter(str.isdigit, list_of_strings))
# print(res)
# for x in res:
    # print(x)

# ls = [10,20,11,13,102,54,45]
# res = list(filter(lambda x: x%2!=0, ls))
# print(res)


# list_of_words = ['one', 'john', 'two', 'list', 'makers','lol']
# res = list(filter(lambda x:len(x)>=4, list_of_words))
# print(res)
#--------------------------------------------------------------------------------------------

# enumerate(iterable) -> возвращает индекс элементов 

# ls = ['str1', 'str2', 'str3']
# for i, x in enumerate(ls):
#     print(x, i)
# res = dict(enumerate(ls))
# print(res)


# fruits = ['apple', 'banana', 'grapes', 'apricot']
# res = list(filter( lambda word : word.startswith('a'), fruits))
# print(res)


# ls = [1,2,3,4,23,45,3,46,76,54]
# res = list(filter(lambda x: x%2==0, ls))
# print(res)


# list_of_words = ['oneOfthelong', 'johnSnow', 'two', 'list', 'makersBootCamp','lol']
# res = list(filter(lambda x:len(x)>=7, list_of_words))
# print(res)





# def chet_(*ls):
#     chet =0
#     nechet =0
#     for i in ls:
#         if i%2==0:
#             chet+=1
#         else:
#             nechet+=1
#     print(f'chet {chet}, nechet {nechet}')
# chet_(1,2,3,4,56,7,8,9)



# def bigthree(*ls):
#   res = all(x > 3 for x in ls )
#   print(res)
# bigthree(1,2,3,4,56)


# ---------------------------------------------------------------------------------------
# zip(iterables) - она соединяет каждый элемент итерируемых элементов между собой в тип данных typlе  и возврашает это 
# ls1 =[1,2,3]
# ls2=[100,200,300]
# res = list(zip(ls1,ls2))
# print(res)

# a = [1, 2, 3, 4, 5]
# b = [10,20,30,40]
# c = [100,200,300]
# print(list(zip(a,b,c)))

# *******************************************************************
# zip for create dict

# d_keys = ['hostname', 'location', 'vendor', 'mmodel', 'IOS', 'IP']
# d_values = ['London', '21 New Bl','Cisco', '4435', '15.4', '10.112.0.2' ]
# dict_r = dict(zip(d_keys, d_values))
# print(dict_r)



# d_keys = ['hostname', 'location', 'vendor', 'mmodel', 'IOS', 'IP']
# d_values = ['London', '21 New Bl','Cisco', '4435', '15.4', '10.112.0.2' ]
# data={
    # 'r1':[ 'London', '21 New Bl','Cisco', '4435', '15.4', '10.112.0.2' ],
    # 'r2': ['London', '21 New Bl','Cisco', '4435', '15.4', '10.112.0.2' ],
    #  
    # }
# date_lond = {}
# for key in data.keys():
    # date_lond[key] = dict(zip(d_keys, data[key]))
# print(date_lond)





# # all and any
# ls = ['rm -rf', 'alias', 'rest']
# comand=input()
# if any([word in comand for word in ls]):
#     raise Exception ('Invalid command')
# print('ok')


# from random import choices
# from string import  ascii_letters, digits
# from itertools import repeat
# q_pas= int(input('Enter sum of passwords: '))
# print({
#     f(choices(ascii_letters, k = 10),choices(digits, k =5)) for f in repeat(lambda x,y: ''.join(set(x+y)), q_pas)
# })