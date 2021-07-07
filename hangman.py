import random
from random import randint
words = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou',
'beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard',
'buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying',
'duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping',
'fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo',
'glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory',
'ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging',
'joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit',
'klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify',
'naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz',
'pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz',
'rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch',
'stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant',
'triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism',
'walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy',
'wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper',
'zodiac','zombie']
def hangman(fails, word, wrong_letters):
    match fails:
        case 0:
            pass
        case 1:
            print('''
                        
                        
                     /   ''')
            print(f'4 trials remaining the wrong letters you have chosen are {wrong_letters}')
        case 2:
            print('''


                     /\   ''')
            print(f'3 trails remaining the wrong letters you have chosen are {wrong_letters}')
        case 3:
            print('''
                     |
                     |
                     /\   ''')
            print(f'2 trials remaining the wrong letters you have chosen are {wrong_letters}')
        case 4:
            print('''
                   --|--
                     |
                     /\   ''')
            print(f'1 trial remining the wrong letters you have chosen are {wrong_letters}')
        case 5:
            print('''                     O
                   --|--
                     |
                     /\   ''')
            print(f'RIP xd the word was {word}')
def check(fails, guess, letters, letter_indices, new_string, wrong_letters):
    if guess in letters:
        for x in range(len(letters)):
            if guess == letters[x]:
                letter_indices.append(x)
        a = list(new_string)
        for b in letter_indices:
            a[b] = guess
        new_string = ''.join(a)
    else:
        fails += 1
        wrong_letters.append(guess)
    return new_string, fails
while 1:
    fails = 0
    wrong_letters = []
    chosen = randint(0, 212)
    word = words[chosen]
    letters  = list(word)
    new_string = under_scores = '_' * len(word)
    print(f'the word is {under_scores}')
    while fails < 5:
        letter_indices = []
        guess = input('guess a letter: ').lower()
        while len(guess) != 1:
            print('invalid guess')
            guess = input('guess a letter: ').lower()
        while guess in wrong_letters or guess in new_string:
            print('you have chosen this letter before')
            guess = input('guess a letter: ').lower()
        new_string, fails= check(fails, guess, letters, letter_indices, new_string, wrong_letters)
        print(new_string)
        hangman(fails, word, wrong_letters)
        if '_' not in new_string:
            print('CONGRATS! you guessed the right word!')
            play_again = input('do you want to play again?\n').lower()
            while play_again != 'yes' and play_again != 'no':
                play_again = input('do you want to play again? (answer with either yes or no)\n').lower()
            match play_again:
                case 'yes':
                    pass
                case 'no':
                    write = 'no'
                    print ('ok bye')
                    break
    play_again = input('do you want to play again?\n').lower()
    while play_again != 'yes' and play_again != 'no':
        play_again = input('do you want to play again? (answer with either yes or no)\n').lower()
    match  play_again:
        case 'yes':
            pass
        case 'no':
            print('ok bye')
            break