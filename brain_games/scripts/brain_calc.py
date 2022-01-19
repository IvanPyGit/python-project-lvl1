import random
import prompt
import time

def calc():
    i = 0
    operators = ['-', '+', '*']
    while i < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operator = random.choice(operators)
        template = '{} {} {}'
        question = template.format(a, operator, b)
        print('Question: ' + question)
        time.sleep(1)
        entered_response = prompt.string("Your answer: ")
        if operator == '-':
            answer = a - b
        elif operator == '+':
            answer = a + b
        else:
            answer = a * b
        if answer == entered_response:
            i += 1
            print('')
        else:
            return ""
    return ("Congratulations, "  "!")

print(calc())