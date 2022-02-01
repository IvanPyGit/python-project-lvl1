import prompt
ROUNDS = 3


def starting_the_game(game):
    print(f'Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}.')
    print(game.DESCRIPTION)
    for _ in range(ROUNDS):
        answer, question = game.get_question_and_answer()
        print(f'Question: {question}')
        entered_response = prompt.string('Your answer: ')
        if entered_response != answer:
            print(f'"{entered_response}" is wrong answer ;(. Correct answer was "{answer}".')
            print(f'Let's try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
