import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 20


def get_question_and_answer():
    start = random.randint(1, 30)
    step = random.randint(1, 10)
    stop = start + step * PROGRESSION_LENGTH
    ap = list(range(start, stop, step))
    hidden_element = random.randint(1, PROGRESSION_LENGTH - 1)
    answer = str(ap[hidden_element])
    ap[hidden_element] = '..'
    question = ' '.join(map(str, ap))
    return answer, question
