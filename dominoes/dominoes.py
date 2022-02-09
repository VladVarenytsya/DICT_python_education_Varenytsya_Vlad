from random import choice

com_pie = []
pla_pie = []
res = []
snake = []
status = 0
r_pie = 0


def start():
    for i in range(7):
        for j in range(i, 7):
            res.append([i, j])


def drop_comp():
    global r_pie
    r_pie = choice(res)
    com_pie.append(r_pie)
    res.remove(r_pie)


def drop_play():
    global r_pie
    r_pie = choice(res)
    pla_pie.append(r_pie)
    res.remove(r_pie)


def drop_all():
    for i in range(7):
        drop_comp()
        drop_play()


def arc():
    global status
    if [6, 6] in com_pie:
        snake.append([6, 6])
        com_pie.remove([6, 6])
        status = 'player'
    elif [6, 6] in pla_pie:
        snake.append([6, 6])
        pla_pie.remove([6, 6])
        status = 'computer'
    elif [5, 5] in com_pie:
        snake.append([5, 5])
        com_pie.remove([5, 5])
        status = 'player'
    elif [5, 5] in pla_pie:
        snake.append([5, 5])
        pla_pie.remove([5, 5])
        status = 'computer'


def fenshui():
    for i in range(1, len(pla_pie)+1):
        print(str(i) + ':', end='')
        print(pla_pie[i-1])


def result():
    print(70 * '=')
    print('Stock size: ' + str(len(res)))
    print('Computer pieces: ' + str(len(com_pie)) + '\n')
    for i in snake:
        print(i, end='')
    print('\n')
    print('Your pieces: ')
    fenshui()
    print('')
    if status == 'computer':
        print('Status: Computer is about to make a move. Press Enter to continue...')
    elif status == 'player':
        print("Status: It's your turn to make a move. Enter your command.")


def cho():
    while len(snake) == 0:
        res.clear()
        com_pie.clear()
        pla_pie.clear()
        start()
        drop_all()
        arc()
    result()


cho()


