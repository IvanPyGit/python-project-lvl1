import random
import prompt
import time
#from brain_even import name
from brain_calc import shell

print('Answer "yes" if the number is even, otherwise answer "no".')


def checking_for_even():
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        if number % 2 == 0:
            answer = "yes"
        else:
            answer = "no"
        question = number
        print('Question: ' + str(number))
        time.sleep(1)
        entered_response = prompt.string("Your answer: ")
        if answer == entered_response:
            i += 1
            print('Correct!')
        else:
            return '''\'yes\' is wrong answer ;(. Correct answer was \'no\'.
Let's try again, ''' "!"

    return ("Congratulations, "  "!")

print(checking_for_even())