import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(2, 100)
    answer = is_prime(question)
    answer = 'yes' if answer is True else 'no'
    return answer, question


def is_prime(question):
    for i in range(2, int(question / 2) + 1):
        if question % i == 0:
            return False
    return True
