import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():

    operators = ['-', '+', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(operators)
    question = '{} {} {}'.format(num1, operator, num2)
    if operator == '-':
        answer = str(num1 - num2)
    elif operator == '+':
        answer = str(num1 + num2)
    else:
        answer = str(num1 * num2)
    return answer, question
