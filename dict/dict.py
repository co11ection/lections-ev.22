# dict() - словарь - > упорядочнооое коллекция эллементоов(python 3.7 -> ordered)
#  каждый элемент всловаре содержится в паре ключ : значение
#   ключи должны быть уникальными и не изменяемым типом данных (str, int, tuple etc.)
# тогда как значениями могут выступать любые типы данных

# this_dic ={
#     'brand':'Ford', 
#     'model':'Mustang', 
#     'year':'1964'
# }
# print(this_dic)


# Hash tables, ассациативный массивб dictionary, object(js) == dictionary(py)

#                                   Способы создания  dictionary
# a = {1,2,3} #set
# a = 1,2,3 # tuple literal(,)



# some_dict = {}
# key_values = {'key':'value', 'key1': 'value1'}
# dict_create_f = dict()
# print(some_dict)

# dict_ = dict((('key', 'value'), ('key1', 'value1')))
# print(dict_)

# -------------------------------------------------------------------------------------------------------------



# user_info={
#     'first_name':'John',
#     'last_name': 'Snow',
#     'age': 21,
#     'email':'johnsnow@mail', 
#     'role':'moderator',
#     'list':[1,2,3]
# }
# print(user_info['first_name'])
# print(user_info.get('age'))
# print(dir(dict))
# print(user_info.items())
# for items in user_info.items():
#     print(items)
# print(user_info.keys())
# user_info['height'] = 185
# print(user_info['height'])
# for value in user_info.values():
#     print(value)

# pop() - удаляет  элемент по определенному ключу
# popitem() -  удаляет последнюю пару в словаре
# user_info.pop('list')
# print(user_info)
# user_info.popitem()
# print(user_info)


# setdefault(key, [defoult_value]) -  работает так же как и метод  get(), но если такого ключа не сущ, то он создаст новую пару значения.

# 1) получение значения


# # dict_ = {
#     'name':'John',
#     'age': 23
# }
# result = dict_.setdefault(age)
# # print(result)

# 2) добавление пары
# dict_ = {
    #  'name':'John',
    #  'age': 23
# }
# result = dict_.setdefault('adres', 'toktogula')
# print(dict_)


# user_info={
    # 'first_name':'John',
    # 'last_name': 'Snow',
    # 'age': 21,
    # 'email':'johnsnow@mail',
    # 'role':'moderator',
    # 'list':[1,2,3]
# }
# print(user_info)
# user_info.update({'first_name': 'raychel'})
# print(user_info)

# __________________________________________________________________________________________________________________---

# roles ={
#     0: 'Admin',
#     1: 'moderator',
#     2: 'vendor',
#     3: 'Cutomer',
#     4: 'guest'
# }
# users = [
#     {
#         'id' : 0,
#         'name': 'John',
#         'roles': roles[0]
#     },
#     {
#         'id':1,
#         'name':'Raychel',
#         'roles': roles[3]
#     },
#     {
#         'id':2,
#         'name':'Aibek',
#         'roles': roles[4]
#     }
# ]

# products = {
#     'id':1,
#     'title': 'Samsung Galaxy S20',
#     'discription': 'Loren Ipsum',
#     'price': 1500
# }
# print(users)
# print(products)


# user_id = int(input(" введите ваш  id: "))
# if users[user_id]['roles'] == roles[0]:
#     products['discrription'] = input(' введите новоеописание продукта: ')
# else:
#     raise Exception('u don\'t have ')
# print(products)

# dict1 = {
#     'tor': 'molot',
#     'age': 23,
#     'abilities':'run'
# }



print(dir(dict))