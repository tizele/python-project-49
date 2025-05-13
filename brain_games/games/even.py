import random



def even():
    number = random.randint(0,100)
    if number % 2 == 0:
        corect = 'yes'
    else:
        corect = 'no'
    return corect, number