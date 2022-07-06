
# def printParams(a,b,c):
#     print(a, '  is stored in a')
#     print(b, '  is stored in b')
#     print(c, '  is stored in c')
#     return 0
# print(printParams(5,33,2))





# *args and **kwargs in function
# def print_scores(student, *scores):
#     print(f'student name : {student}')
#     # print(args)
#     # print(type(args))
#     for x in scores:
#         print(x)
# print(print_scores('john', 100,10,70,43,56))
# import sys
# sys.e

# def print_pet_names(owner, **pets):
    # print(f'owneR NAME {owner}')
    # print(pets)
# 
# print(print_pet_names('John', dog = 'rex', cat='larry', fish = ['nemo', 'dory'], turtle = 'leonardo'))


# def get_some_data(a,b, *args, **kwargs):
#     print('params a & b ', a,b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print(args)
#     print(kwargs)
# get_some_data(1,2,3,4,lang ='python', name = 'john', lol ='pip')


# def conc_two_str(str1,str2):
#     import random
#     res = random.randint(1,10)
#     return str1+str2+str(res)

# result = conc_two_str('hello', 'world')
# print(result)


# def generate_pasword(name, fam):
#     import random
#     random_num = random.randint(100000,999999)
#     return name+fam+'_'+str(random_num)

# def get_info():
#     name = input('enter name ')
#     fam = input('enter fam ')
#     return generate_pasword(name, fam)
# result = get_info()
# print(result)




# def generate_random_string(len_, lang):
#     import string as s
#     import random
#     random_str = ''.join(random.choice(s.ascii_lowercase + s.digits) for i in range(0,len_))
#     return random_str
# def get_len():
#     len_ = int(input())
#     return generate_random_string(len_, 'eng')

# print(get_len())

##################################################################################
# from ast import main


# def add(num1, num2): return num1 + num2
# def subtract(num1,num2): return num1 - num2
# def multiply(num1,num2): return num1* num2
# def devide(num1, num2): 
#     try:
#         return num1/ num2
#     except ZeroDivisionError:
#         return 'you can\'t devide by 0'

# def main():
#     try:
#         num1 = float(input('enter 1 num: '))
#         num2 = float(input('enter 2 num: '))
#     except ValueError:
#         print('you enter incorect value')
#         main()
#     def operator(operator_):
#         operator_ = input('Enter operator (+, -, /, *): ')
#         if operator_ =='+': result=add(num1, num2)
#         result = None

#         if operator_ =='+': result=add(num1, num2)
#         elif operator_ == '-': result = subtract(num1,num2)
#         elif operator_ == '*': result = multiply(num1,num2)
#         elif operator_ == '/': result = devide(num1,num2)
#         else: 
#             print('you enter incorrect operator') 
#             operator()
#         print(f'result {result}')

#     question = input('Are you want contuine? (Yes/No): ')
#     if question.lower() == 'yes':
#         main()
#     else:
#         print('thanks for using')
# main()