import math
import random


def prime():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = random.randint(1, 1000)
    numer_sqrt = math.floor(math.sqrt(number))
    corect = 'yes'
    for i in range(2, numer_sqrt):
        if number % i == 0:
            i = numer_sqrt
            corect = 'no'
    return corect, number, rules
        
    


        



