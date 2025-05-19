import random


def gcd():
    rules = 'Find the greatest common divisor of given numbers.'
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    number = f'{number_1} {number_2}'
    i = True
    if number_1 < number_2:
        if number_2 % number_1 == 0:
            gcd = number_1
        else:
            gcd = number_1 // 2
            while i:
                if number_1 % gcd == 0 and number_2 % gcd == 0:
                    i = False
                else: 
                    gcd -= 1
    else:
        if number_1 % number_2 == 0:
            gcd = number_2
        else:
            gcd = number_2 // 2
            while i:
                if number_1 % gcd == 0 and number_2 % gcd == 0:
                    i = False
                else: 
                    gcd -= 1
    corect = gcd
    return int(corect), number, rules
