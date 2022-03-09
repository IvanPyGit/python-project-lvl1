import prompt

ROUNDS_COUNT = 3


def starting_the_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}.')
    print(game.DESCRIPTION)
    for _ in range(ROUNDS_COUNT):
        answer, question = game.get_question_and_answer()
        print(f'Question: {question}')
        correct_answer = prompt.string('Your answer: ')
        if correct_answer != answer:
            print(f'"{correct_answer}" is wrong answer ;(. '
                  f'Correct answer was "{answer}".')
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
