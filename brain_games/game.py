import random
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_calc import calc


def greet():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    parity_check(name)
    

def parity_check(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        corect, number = calc()
        print(f'Question: {number}')
        answer = prompt.string(f'Your answer: ')
        if answer == str(corect):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Corect answer was '{corect}'.")
            print(f"Let's try again, {name}")
            i = 0
    print(f'Congratulation, {name}!')