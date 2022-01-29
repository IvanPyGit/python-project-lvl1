import random


rules_game = 'What is the result of the expression?'
def calc():
    operators = ['-', '+', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(operators)
    question = '{} {} {} = '.format(num_1, operator, num_2)
    if operator == '-':
        answer = num1 - num2
    elif operator == '+':
        answer = num1 + num2
    else:
        answer = num1 * num2
    return [answer, question]