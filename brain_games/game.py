import prompt

from brain_games.cli import welcome_user


def game(names):
    _, _, rules = names()
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print(rules)
    NUMBER_CORRECT_ANSWER = 3
    for i in range(NUMBER_CORRECT_ANSWER):
        crt, quest, _ = names()
        print(f'Question: {quest}')
        answer = prompt.string('Your answer: ')
        if answer == str(crt):
            print('Correct!')
            if i == NUMBER_CORRECT_ANSWER - 1:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Corect answer was '{crt}'.")
            print(f"Let's try again, {name}!")
            break