import random


DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 20 + 1

def get_question_and_answer():
    start = random.randint(1, 30)
    step = random.randint(1, 10)
    stop = start + step * LENGTH_PROGRESSION
    ap = list(range(start, stop, step))
    length = len(ap)
    hidden_element = random.randint(1, length - 1)
    answer = str(ap[hidden_element])
    ap[hidden_element] = '..'
    question = ' '.join(map(str, ap))
    return answer, question
