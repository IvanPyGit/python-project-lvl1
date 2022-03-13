import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 20


def get_question_and_answer():
    start = random.randint(1, 30)
    step = random.randint(1, 10)
    stop = start + step * PROGRESSION_LENGTH
    progression = list(range(start, stop, step))
    hidden_element = random.randint(1, PROGRESSION_LENGTH - 1)
    answer = str(progression[hidden_element])
    progression[hidden_element] = '..'
    question = ' '.join(map(str, progression))
    return answer, question
