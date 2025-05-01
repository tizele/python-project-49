import random
import prompt
from brain_games.cli import welcome_user

if __name__ == "__main__":
    main()

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    parity_check(name)

def parity_check(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0,1000)
        if number % 2 == 0:
            corect = 'yes'
        else:
            corect = 'no'
        print(f'Question: {number}')
        answer = prompt.string(f'Your answer: ')
        if answer == corect:
            print('Correct!')
            i += 1
        elif answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Corect answer was 'no'.")
            print(f"Let's try again, {name}")
            i = 0
        elif answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Corect answer was 'yes'.")
            print(f"Let's try again, {name}")
            i = 0
    print(f'Congratulation, {name}!')



