import random


def gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{} {} = '.format(num1, num2)
    for i range(1, (max(num1, num2) + 1))
        if((num1 % i == 0) and (num2 % i) == 0):
            answer = i
    return [answer, question]