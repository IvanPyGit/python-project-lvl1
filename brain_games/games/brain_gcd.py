import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{} {}'.format(num1, num2)
    answer = gcd(num1, num2)
    return answer, question


def gcd(num1, num2):
    answer = str(math.gcd(num1, num2))
    return answer
