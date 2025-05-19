import math
import random


def prime():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = random.randint(1, 5)
    numer_sqrt = int(math.sqrt(number))
    corect = 'yes'
    for i in range(1, numer_sqrt):
        if number % i == 0:
            i = numer_sqrt
            corect = 'no'
    return corect, number, rules
        
    


        



