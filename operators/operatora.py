# operatory sravnenia
# uslovnye operatory
# logicheskie operatory
#*******************************************************************************************************************
# operatoy sravnenia: <, >, <=,>=, ==, !=
# num1 = 15
# num2 = 30
# result =  num1 == num2
# print(result)
# ******************************************************************************************************************
# ord - dlia proverki ascii-code
# bool ----- True(1), False(0)
# chr () dlia ascii coda
# ******************************************************************************************************************
# uslovnye operatory 
# if <condition>
#    if comdition = true
#    <body if> 
# elif < condition elif >
#    if condition = false
#    <elif body>  
# else 
# <body> 
# *****************************************************************************************************************
# string = input('enter smth: ')
# if string == 'hello':
    # print('hello stranger')
# elif string == 'mers':
    # print('mrs sls')
# else:
    # print('sonpodenia netu')


# sing up 

# emil = input('enter email:')
# password1 =input('enter pasword: ')
# password2 = input('enter password confirmitional: ')
# 
# if password1 != password2:
    # raise Exception('password did\'t match')
# else:
    # print('successfully signed up')


# 2
# age = input('enter your age: ')
# if age.isdigit(): #.isdigit function for proveri stroki
#     age = int(age)
# else:
#     print('vvedite corectnye dannye')
#     raise Exception('Value error')

# if age < 18:
#     print(f'chuvak come after {18-age}')
# else:
#     print('you\'r wellcome') 
# ************************************************************************************
# logical operators
# 1) and --> logical и
# 2) or --> logical  или
# 3) not --> logical отрицание


# age =20
# smage = 18
# result = age and smage >10
# lol = age < 20 or smage>10
# obb = not age !=40 or not smage<19
# print(lol)
# print(result)
# print(obb)
# 
# userGoogleUser = False
# userGithubUser = True
# userAgeGreater = False
# userAccountsCoins = 8000
# 
# if userGoogleUser and userGithubUser and userAgeGreater:
    # print('you can enter the system mr John Snow')
# else:
    # print('Sorry you should have Google and Github accounts' )
# 
# if userGoogleUser or userGithubUser or userAccountsCoins<1000:
    # print('you can enter the system mr John Snow')
# else:
    # print('Sorry you should have Google and Github accounts' )
# if not userGoogleUser and not userGithubUser:
    # print('you can enter the system mr John Snow')
# else:
    # print('Sorry you should have Google and Github accounts' )