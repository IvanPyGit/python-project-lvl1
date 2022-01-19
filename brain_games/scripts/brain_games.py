#!/usr/bin/env python
import prompt

def greet():
    print("Welcome to the Brain Games!")

def main():
    greet()

if __name__ == '__main__':
    main()

def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello, " + name)