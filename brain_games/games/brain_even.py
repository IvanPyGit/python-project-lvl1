import random


def checking_for_even():
        question = random.randint(1, 100)
        answer = 'yes' if question % 2 == 0 else 'no'
        return [answer, question]

rules_game = 'Answer "yes" if the number is even, otherwise answer "no".'
