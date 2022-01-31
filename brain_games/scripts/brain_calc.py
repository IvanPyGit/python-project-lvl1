#!/usr/bin/env python3
from brain_games.games import brain_calc
from brain_games.engine import starting_the_game


def main():
    starting_the_game(brain_calc)


if __name__ == '__main__':
    main()