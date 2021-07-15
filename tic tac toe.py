chosen = 0
moves = 0
board = ['''
   ''','1','  | ','2',' |  ','3',
'''\n------|---|------
   ''','4','  | ','5',' |  ','6',
'''\n------|---|------
   ''','7','  | ','8',' |  ','9'
]
def win():
    letter = ''
    yes = False
    x = board[1]
    if board[3] == x:
        if board[5] == x:
            yes = True
            letter = x
    if x == board[7]:
        if x == board[13]:
            yes = True
            letter = x
    if x == board[9]:
        if x == board[17]:
            yes = True
            letter = x
    y = board[3]
    if y == board[9]:
        if y == board[15]:
            yes = True
            letter = y
    z = board[5]
    if z == board[11]:
        if z == board[17]:
            yes = True
            letter = z
    a = board[7]
    if a == board[9]:
        if a == board[11]:
            yes = True
            letter = a
    b = board[13]
    if b == board[15]:
        if b == board[17]:
            yes = True
            letter = b
    return letter, yes
def check(index, letter, moves):
    if board[index] == 'X' or board[index] == 'O':
        print('this space is already taken')
        moves = moves
    else:
        board[index] = letter
        moves = moves + 1
    return moves
def game(letter, moves):
    answer = input(f'where  do you want to put the {letter}?\n').lower()
    while answer not in answers:
        print('this is not a valid answer')
        answer = input('please input a valid answer\n').lower()
    match answer:
        case '1':
            moves = check(1, letter, moves)
        case '2':
            moves = check(3, letter, moves)
        case '3':
            moves = check (5, letter, moves)
        case '4':
            moves = check(7, letter, moves)
        case '5':
            moves = check (9, letter, moves)
        case  '6':
            moves = check(11, letter, moves)
        case '7':
            moves = check(13, letter, moves)
        case '8':
            moves = check(15, letter, moves)
        case '9':
            moves = check(17, letter, moves)
        case 'help':
            print('its very simple just type a number to choose it')
    return moves


answers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'help']
x = ''.join(board)
print(f'''{x}
type help for the list of commands''')
while 1:
    if  moves % 2 == 0:
        moves = game('X', moves)
        x = ''.join(board)
        print(x)
        letter, yes = win()
        if yes:
            print(f'{letter} won. CONGRATS!')
            break
        for x in answers[:9]:
            if x.upper() not in board:
                chosen += 1
        if chosen >= 9:
            print('no moves left. game over')
            break
        chosen = 0
    else:
        moves = game('O', moves)
        x = ''.join(board)
        print(x)
        letter, yes = win()
        if yes:
            print(f'{letter} won. CONGRATS!')
            break
        for x in answers[:9]:
            if x.upper() not in board:
                chosen += 1
        if chosen >= 9:
            print('no moves left. game over')
            break
        chosen = 0
