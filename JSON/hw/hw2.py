# 1

# fname = input('Файл: ')
# f = open(fname,'w')
# while True:
#     s = input('Enter text: ')
#     if s == '': 
#         break
#     f.write(s+'\n')
# f.close()

# 2

# with open('text.txt') as f:
#     line = 0
#     for i in f:
#         line += 1

#         flag = 0
#         word = 0
#         for j in i:
#             if j != ' ' and flag == 0:
#                 word += 1
#                 flag = 1
#             elif j == ' ':
#                 flag = 0
 
#         print(i,len(i),'симв.',word,'сл.')
 
#     print(line,'стр.')

# 3

# with open("text.txt") as file:
#     counter = summa = 0
#     for line in file:
#         counter += 1
#         length_line = len(line)
#         for i in range(length_line):
#             if line[i].isdigit():
#                 num = int(line[i])
#                 summa += num
#                 if num < 3:
#                     with open('uch.txt', 'a') as f:
#                         f.write(line)
                    
#                 break
 
#     sred = counter / summa
#     with open('uch.txt', 'a') as f:
#         f.write(f"\nСредний бал по классу: {sred}")


















# 4


# def office_google():
#     print('google office data: \n1) google_kazakstan.txt \n2) google_paris.txt \n3) google_poland.txt \n4) google_kyrgyzstan.txt \n5) google_san_francisco.txt \n6) google_germany.txt \n7) google_moscow.txt \n8) google_sweden.txt')
#     choise = int(input('Enter your choise: '))
#     if choise == 1:
#         with open('google_kazakstan.txt', 'a') as f:
#             data = f.writelines(input('Enter your complaint: ')+'\n')
#     elif choise == 2:
#         with open('google_paris.txt', 'a') as f:
#             data = f.write(input('Enter your complaint: ')+'\n')
#     elif choise == 3:
#         with open('google_poland.txt', 'a') as f:
#             data = f.write(input('Enter your complaint: ')+'\n')
#     elif choise == 4:
#         with open('google_kyrgyzstan.txt', 'a') as f:
#             data = f.write(input('Enter your complaint: ')+'\n')
#     elif choise == 5:
#         with open('google_san_francisco', 'a') as f:
#             data = f.write(input('Enter your complaint: ')+'\n')
#     elif choise == 6:
#         with open('google_germany.txt', 'a') as f:
#             data = f.write(input('Enter your complaint: ')+'\n')
#     elif choise == 7:
#         with open('google_moscow.txt', 'a') as f:
#             data = f.write(input('Enter your complaint: ')+'\n')
#     elif choise == 8:
#         with open('google_sweden.txt', 'a') as f:
#             data = f.write(input('Enter your complaint: ')+'\n')
#     else:
#         print('Invaliad choise')
#     def ask_q():
#         ask = input('Do you want contuine: y/n: ')
#         if ask.lower() == 'y':
#             office_google()
#         elif ask.lower() == 'n':
#             print('Good bye')
#         else:
#             print('Invalid choise')
#             ask_q()
#     ask_q()
# office_google()














