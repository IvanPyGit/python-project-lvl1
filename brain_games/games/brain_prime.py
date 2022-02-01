import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(1, 100)
    for i in range(2, int(question / 2 + 1)):
        if question % i == 0:
            answer = 'no'
            return answer, question
    answer = 'yes'
    return answer, question
