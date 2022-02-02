import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 30)
    stop = random.randint(80, 150)
    step = random.randint(1, 10)
    ap = list(range(start, stop, step)[:20])
    length = len(ap)
    hidden_element = random.randint(1, length)
    answer = str(ap[hidden_element])
    ap[hidden_element] = '..'
    question = ' '.join(map(str, ap))
    return answer, question
