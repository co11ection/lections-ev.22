# области видимости и пространств имен
#  Build-in(встроенная )-- print, len, max
#  Global 
#  enclosed(не локальная, nonlocal)
#  local 


# def print_list(some_list):
#     for elements in some_list:
#         print(elements)
# element = 'q'
# print_list([1,2,3,4,5])
# print(element)




# a =10 # global
# print #built
# def hello(): #global
#     a = 'hello' #local
#     print(a, 'local')
# hello()
# print(a, 'global')


# x = 'gloal'
# print(x, '1')
# def enclosed():
#     x = 'enclosed'
#     def local():
#         x ='local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')
# enclosed()
# print(x, '5')



# var = 100
# def increment():
#     global var
#     var +=1
# increment()
# print(var)


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num+=1
#         return num
#     return increment
    
# c = counter()
# print(c())



# ls = [[1,2,3], [3,3,5]]
# # sums = []
# for i in ls: 
    
#     sums.append(sum(i))
    
# print(max(sums))
# res=max([(sum(x)) for x in ls])
# print(res)


# game = [1,2,3]
# alice =[13,15,38]
# john =[5,15,50]
# def compareScores(a,j):
#     score_a = 0
#     score_b = 0
#     for i  in range(0, len(a)):
#         if a[i]>j[i]:
#             score_a+=1
#         elif j[i]>a[i]:
#             score_b+=1
#         else:
#             pass
#     return {"alice":score_a, 'John': score_b}
# print(compareScores(alice, john))





# str_ = 'pythoniiist'
# 
# dict_ = {key:str_.count(key) for key in str_}
# print(dict_)




