import random
from random import randint
def number(start, end, trials):
    number = randint(start, end)
    guess = int(input(f'I have chosen a random number from {start} to {end} try to guess that number!\n'))
    while guess != number:
        trials += 1
        if number > guess:
            guess = int(input('your guess is too low try going higher!\n'))
        else:
            guess = int(input('your guess is too  high try going lower!\n'))
    print(f'you have guess the right number, {number}, in {trials} trials')

while True:
    trials = 0
    difficulty = input('what difficulty do you want to play on? (easy, normal, hard, or insane)\n').lower().strip()
    while difficulty != 'easy' and difficulty != 'normal' and difficulty != 'hard' and difficulty != 'insane':
        difficulty = input('please choose a valid answer. what difficulty do you want to play on? (easy, normal, hard, or insane)\n').lower().strip()
    match difficulty:
        case  'easy':
            number(start = 1, end = 10, trials = trials)
        case 'normal':
            number(start = 1, end = 100, trials = trials)
        case 'hard':
            number(start = 1, end = 1000, trials = trials)
        case 'insane':
            number(start = 1, end = 100000, trials = trials)
    retry = input('do you want to play again?\n').lower().strip()
    while retry != 'yes' and retry != 'no':
        retry = input('please  type a valid answer do you want to try again? (yes or no)\n').lower().strip()
    match retry:
        case 'yes':
            pass
        case 'no':
            break