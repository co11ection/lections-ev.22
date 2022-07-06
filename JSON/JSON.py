

# JavaScript Object Notation JSON
#  Единый формат хранения и передачи данных между компьютераи, сервисами , приложениями и языками программирования через сеть интернет
# <file_name>.json

# {
    # 'id':1,
    # "author":'johns',
    # 'posts':[]
# } это Json,задача науч переводить Json  python dict


# |||
# JS object == {}
# PY dict == {}
# JSON ==={}


# Процессы стереолизации данных и их десесрилизация 

# Сериализация (запись данных  в JSON) -  это перевод pY dict в  JSON формат (либо сохр все в файл или сохр как текстовый файл) 
# dump -- метод записывает обьект в PYTHON в файл в формате JSON
# dumps -- метод записывает обьект в PYTHON в строку в формате JSON

# Десесрилизация (чтение данных и JSON) -- это процесс перевода из JSON в PY dict
# load -- метод который считывает обЪект в формате JSON и переводи в PY Object
# loads --метод который считыват JSON в текстовом формате и переводит в PY Oblect

# ##########################################################################################################################################################
# Процесс десесрелизации

# import json
# from urllib.request import urlopen

# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# # print(data)
# generate_to_dict = json.load(data)
# print(generate_to_dict)


# import json
# with open('downApi.json','r') as file:
#     data = file.read()
#     # print(data)
#     user = json.loads(data)
#     print(user)
#     print(type(user))


##############################################################################################################################################################
# Процесс стериолизации
# import json
# dict_ = {
#     'name': 'John',
#     'last':'Snow',
#     'status': True,
#     'wife': None,
#     'children': False
# }

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# import json
# dict_ = {
#     'name': 'John',
#     'last':'Snow',
#     'status': True,
#     'wife': None,
#     'children': False
# }
# string = json.dumps(dict_)
# print(string)
# print(type(string))


# C - create 
# R - retrieve(read)
# U - update
# D - delete


