import random


def progression():
    rules = 'What number is missing in the progression?'
    number_1 = random.randint(1,30)
    number_2 = random.randint(1,30)
    len = random.randint(5,10)
    quest = random.randint(1,len)
    pgs = []
    if number_1 > number_2:
        b = number_1 - number_2
        pgs.append(number_2)
    else: 
        b = number_2 - number_1
        pgs.append(number_1)
    for i in range(len):
        pgs.append(pgs[i] + b)
    corect = pgs[quest]
    pgs[quest] = '..' 
    number = ' '.join([str(x) for x in pgs])
    return corect, number, rules

    


