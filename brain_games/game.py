import random
import prompt
from brain_games.cli import welcome_user


def game(names):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        corect, quest = names()
        print(f'Question: {quest}')
        answer = prompt.string(f'Your answer: ')
        if answer == str(corect):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Corect answer was '{corect}'.")
            print(f"Let's try again, {name}")
            i = 0
    print(f'Congratulation, {name}!')