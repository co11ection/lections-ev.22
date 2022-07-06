#############################################################################################################

# #  1
# ls = [i for i in range(0,200,2) ]
# print(ls)
# # 2
# a = [i for i in range(200) if (i%2==0) and (i%3==0) ]
# print(a)
# # 3
# b = [pow(i,2) if i%2==0 else i for i in range(100)]
# print(b)

##############################################################################################################

# new_list = [expression, for item in iterable <if condition==True>]

##############################################################################################################

# ls=[pow(i,2) for i in range(0,11)]
# print(ls)

##############################################################################################################

# fruits1 = ['apple','banana', 'mango', 'kiwi', 'lemon']
# fruits = [x.title() for x in fruits1]
# print(fruits)


# fruits = [i for i in fruits1 if i == 'cherry']
# print(fruits)

##############################################################################################################

# list_ = [[1,2,3],[4,5,6],[7,8,9]]
# ls = [x for list1 in list_ for x in list1]
# print(ls)

##############################################################################################################

# import datetime
# start = datetime.datetime.now()
# # ls=[]
# # for x in range(1,100000):
# #     ls.append(x)
# # finish = datetime.datetime.now()
# # print(ls, finish - start)
# ls = [i for i in range(10000000000)]
# finish = datetime.datetime.now()
# print(ls, finish-start)

x = int(input('введиет число: ')) 
dict_ = { n:pow(n,2) for n in range(1,501) if n%x == 0
}
print(dict_)