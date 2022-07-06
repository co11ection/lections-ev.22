# 1

# with open('task1.txt', 'r') as f:
#     for x in range(5):
#         data = f.readline()
#         print(data)

# 2

# for i in open('task2.txt'):
#     print(i)

# 3
# with open('task3.txt', 'w') as file:
#     data = file.write(input('enter nums with spaces: '))

# 4
# with open('task4.txt', 'w') as file:
#     for i in range (1,16):
#         if i == 15:
#             data = file.writelines(str(i))
#         else:
#             data = file.writelines(str(i)+'\n')
# with open('task4.txt') as f:
#     count = sum(1 for line in f)
#     print(count)

# 5

# with open('task4.txt', 'r') as file:
#     m = []
#     full_f = file.read()
#     for i in full_f.split():
#         m.append(int(i))
# with open('task5.txt', 'w') as fs:
#     print('max_num = ', max(m), file=fs)
#     print('min_num = ', min(m),file=fs)
        