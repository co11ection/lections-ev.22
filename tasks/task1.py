

# uroven = 0
# ls = []
# def count_steps(steps,  ls ):
    # step = int(input('Enter num step: '))
    # for i in range(step):
        # lol = input('Enter steps')
        # ls.append(lol)
        # for x in ls:
            # if x == 'u':
                # i+=1
            # else:
                # i-=1
# 




def counting(path):
    dolina = 0
    sea_level = 0
    for x in path:
        if x =='U':
            sea_level +=1
            if sea_level == 0:
                dolina += 0
        elif x =='D':
            sea_level -=1
    return dolina
print(counting('DDUUDDUDUUDD'))
