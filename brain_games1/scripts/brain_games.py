#!/usr/bin/env python
import prompt
import brain_even
ROUNDS = 3


def StartingTheGame(answer, question):
    SeriesOfCorrectAnswers = 0
    name = prompt.string("May I have your name? ")
    print('Welcome to the Brain Games!')
    print(f'Hello, {name}.')
    while SeriesOfCorrectAnswers < ROUNDS:
        brain_even.checking_for_even()
        print(f'Question: {question}')
        entered_response = prompt.string("Your answer: ")
        if entered_response == answer:
            print('Correct!')
            SeriesOfCorrectAnswers += 1
        else:
            print(f'"{entered_response}" is wrong answer ;(. Correct answer was "{answer}". \nLet\'s try again, {name}!')
            return 0
    return f'Congratulations, {name}!'

