import random


def calc():
    rules = 'What is the result of the expression?'
    number_1 = random.randint(0, 20)
    number_2 = random.randint(0, 20)
    number = f'{number_1} {random.choice(['+', '-', '*'])} {number_2}'
    corect = eval(number)
    return corect, number, rules