import random
from random import randint
while True:
    start = input ('do you want to roll a die?\n').lower()
    while start != 'yes' and start != 'no':
        start = input('''please enter a valid answer (yes or no
do you want to roll a die?\n''').lower()
    match start:
        case 'yes':
            print(f'the number you got is {randint(1, 6)}')
        case 'no':
            print ('k.')
            break