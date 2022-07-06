import random

ls = ['plov', ' manty', 'kuurdak', 'lagman']
p =0
m = 0
k = 0
l = 0
for i in range(0,10000):
    choise = random.choice(ls)
    if choise.lower() == 'plov':
        p+=1
    elif choise.lower() == 'manty':
        m+=1
    elif choise.lower() == 'kuurdak':
        k+=1
    else:
        l+=1
# x = max(p,m,k,l)
# if x == p:
#     print(f'plov{p}')
# elif x ==m:
#     print(f'manty{m}')
# elif x == k:
#     print(f'kuurdak{k}')
# else:
#     print(f'lagman{l}')
dict_ = {
    'Plov':p, 'manty': m, 'kuurdak':k, 'lagman': l
}
print(dict_.items())
res = sorted(dict_.items(), key = lambda x: x[1])
winer = res[-1]
print(f'win dish {winer[0]}, he get {winer[1]} scores')