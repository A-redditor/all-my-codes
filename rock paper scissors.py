import random
from random import randint
CompPoints = 0
PlayerPoints = 0
while True:
    choice = input ('what do you choose: rock, paper, or scissors? (type quit to end the game) \n').lower()
    while choice != 'rock' and choice != 'paper' and choice != 'scissors' and choice != 'quit':
        print ('this is not a valid choice')
        choice = input ('please write a valid choice: ')
    CompChoice = randint(1, 27)
    match choice:
        case 'rock':
            if CompChoice <= 9:
                print ('I choose rock. its a draw!')
            elif CompChoice >9 and CompChoice <= 18:
                print ('I choose paper. I win!')
                CompPoints  += 1
            else:
                print (' I choose scissors. you win!')
                PlayerPoints += 1
        case 'paper':
            if CompChoice <= 9:
                print('I choose rock. you win!')
                PlayerPoints += 1
            elif CompChoice > 9 and CompChoice <= 18:
                print('I choose paper. its a draw!')
            else:
                print('I choose scissors. I win!')
                CompPoints += 1
        case 'scissors':
            if CompChoice <= 9:
                print('I choose rock. I win!')
                CompPoints += 1
            elif CompChoice > 9 and CompChoice <= 18:
                print('I choose paper. you win!')
                PlayerPoints += 1
            else:
                print('I choose scissors. its a draw!')
        case 'quit':
            break
    print (f'''my score is {CompPoints}
your score is {PlayerPoints}''')