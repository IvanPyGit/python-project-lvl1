import prompt
ROUNDS = 3


def starting_the_game(game):
    question, answer = game.checking_for_even()
    series_of_correct_answers = 0
    name = prompt.string("May I have your name? ")
    print('Welcome to the Brain Games!')
    print(f'Hello, {name}.')
    while series_of_correct_answers < ROUNDS:
        print(f'Question: {question}')
        entered_response = prompt.string("Your answer: ")
        if entered_response == answer:
            print('Correct!')
            series_of_correct_answers += 1
        else:
            print(f'"{entered_response}" is wrong answer ;(. Correct answer was "{answer}". \nLet\'s try again, {name}!')
            return 0
    return f'Congratulations, {name}!'
