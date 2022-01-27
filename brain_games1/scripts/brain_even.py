import random
import brain_games

def checking_for_even():
        number = random.randint(1, 100)
        question = number
        answer = 'yes' if brain_games.entered_response % 2 == 0 else 'no'

def a():
        print('Answer "yes" if the number is even, otherwise answer "no".')
        brain_games.StartingTheGame(answer, question)

a()