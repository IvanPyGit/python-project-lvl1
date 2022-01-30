from brain_games.scripts.brain_games import main
from brain_games.cli import welcome_user
import prompt
ROUNDS = 3


def starting_the_game(game):
    main()
    name = f'{welcome_user()}'
    answer, question, rules_game = game.checking_for_even()
    print(rules_game)
    series_of_correct_answers = 0
    while series_of_correct_answers < ROUNDS:
        answer, question, rules_game = game.checking_for_even()
        print(f'Question: {question}')
        entered_response = prompt.string("Your answer: ")
        if entered_response == answer:
            print('Correct!')
            series_of_correct_answers += 1
        else:
            print(f'"{entered_response}" is wrong answer ;(. Correct answer was "{answer}". \nLet\'s try again, {name}!')
            return 0
    return f'Congratulations, {name}!'
