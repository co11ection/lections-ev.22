#  обработка  исключений 
########### Оперраторы try..except ####################
# ошибки  связанные с кодом:

# IndentationError
# TabError
# SyntaxError

# #  исключения -> invalide Values
# ZeroDivisionError
# KeyError
# ValueError
# ImportError
# BaseException  #прородитель ошбок
# NameError
# ArithmeticError
# IndexError

# try ... except

# try:
    # <body try>
# except:
    # <body except>

# try:
#     num1 = int(input('enter num: '))
#     print(num1)
# except:
#     print('u don\'t enter int')
# print('most important string')

# import sys
# list_ = [1,2,3,4,5]
# index_ = int(input('enter index: '))
# try:
#     res = list_[index_]
#     print(res)
# except:
#     import sys
#     print(f'oops, we catch {sys.exc_info()[0]} error')



# list_ = [1,2,3,4,5]
# index_ = int(input('enter index: '))
# try:
#     res = list_[index_]
#     print(res)
# except Exception as e:
#     import sys
#     print(f'oops, we catch {e.__class__} error')


# list_ = [1,2,3,4,5]

# try:
#     index_ = int(input('enter index: '))
#     res = list_[index_]
#     print(res)
# except IndexError:
#     print('IndexError')
# except ValueError:
#     print('ValueError')


# else  в  try ... except
# finally  в try .. except
# try:
#     <body>
# except:
#     <body>
# else:
#     <body>  #  если  в операторе try  не случилась ошибка 
# finally:
    # <body> #  сработает в любом случае



# 
