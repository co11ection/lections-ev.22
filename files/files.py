# работа  файлами 
#  каретка - указатель.



# open(<путь до нашего файла>)

# file = open('home/hello/Desktop/ev.22/files/files.py') #абсолютный путь
# file = open('files.py')#относительный путь
# print(file)
# 

#режимы для работы с файлами


# 1) r/r+ (read)
# 2) w/w+ (write)
# 3) a/a+ (append)
# t, b, x

# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(type(data))





# file = open('/home/hello/Desktop/ev.22/files/text.txt')
# data = file.readlines()
# print(data)
# file.close()

# file = open('text.txt', 'w')
# file.write('hello')
# file.close()

# file = open('text.txt', 'a')
# file.write('\n 19 years old')
# file.close()



#  Контекстный менеджер
# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)



# ls = ['hello', 'lol', 'bib']
# with open('text.txt', 'w') as f:
    # f.writelines(line +'\n' for line in ls)

# file.tell()-->озвращвет индекс где находится коретка(указатель)
# file.seek(<int>) -- перемещает каретку (указаель) на указанный int(index)
# __________________________________________________________________________________________


# from PIL import Image
# import pytesseract
# import re
# def get_image_codes(list_images):
#     lis_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         lis_of_imei.append(re.findall(r'IME. \d.\s', string))
# list_images = ('imei.jpg',)
# get_image_codes(list_images)