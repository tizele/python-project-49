import random


def even():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = random.randint(0, 100)
    if number % 2 == 0:
        corect = 'yes'
    else:
        corect = 'no'
    return corect, number, rules