#!/usr/bin/env python3
from brain_games.engine import starting_the_game
from brain_games.games import brain_gcd


def main():
    starting_the_game(brain_gcd)


if __name__ == '__main__':
    main()
