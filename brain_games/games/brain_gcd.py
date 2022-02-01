import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{} {}'.format(num1, num2)
    for i in range(1, (max(num1, num2) + 1)):
        if((num1 % i == 0) and (num2 % i == 0)):
            answer = str(i)
    return answer, question
