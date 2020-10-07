"""The module contains the basic rules and logic of the game."""

from random import randint

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)
MIN_PRIME = 2


def generate_round():
    """Return the main logic of the game.

    Returns:
        game_question: equation description;
        game_answer: result of operation

    """
    number = randint(MIN_PRIME, 100)
    game_question = '{0} is prime?'.format(number)
    if is_prime(number):
        return game_question, 'yes'
    return game_question, 'no'


def is_prime(n):
    """Return True if number is prime."""
    d = MIN_PRIME
    while d <= n ** 0.5:
        if n % d == 0:
            return False
        d += 1
    return True
