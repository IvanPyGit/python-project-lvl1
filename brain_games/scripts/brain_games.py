#!/usr/bin/env python
from brain_games.cli import welcome_user


def welcome():
    print('Welcome to the Brain Games!')

def main():
    welcome()
    name = welcome_user()
    return name

print(name)

if __name__ == '__main__':
    main()
