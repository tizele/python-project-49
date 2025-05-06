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
        number_1 = random.randint(0,20)
        number_2 = random.randint(0,20)
        number = f'{number_1} {random.choice(['+','-','*'])} {number_2}'
        corect = eval(number)
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
 

