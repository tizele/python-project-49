from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import parity_check


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
#parity_check(name)
    


if __name__ == "__main__":
    main()