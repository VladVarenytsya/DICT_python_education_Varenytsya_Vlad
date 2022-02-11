from random import choice

com_pie = []
pla_pie = []
res = []
snake = []
status = 0
r_pie = 0
pla_in = 0
dra = []


def he_ha():
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


def snake_v():
    if len(snake) < 7:
        for i in snake:
            print(i, end='')
    elif len(snake) > 6:
        for i in range(6):
            if i < 2:
                print(snake[i], end='')
            elif i == 2:
                print(snake[i], end='...')
            elif i > 2:
                print(snake[i-6], end='')
        

def f_res():
    if status == 'computer':
        print('Status: Computer is about to make a move. Press Enter to continue...')
    elif status == 'player':
        print("Status: It's your turn to make a move. Enter your command.")
    elif status == 'draw':
        print("Status: The game is over. It's a draw!")
    elif status == 'pla_w':
        print("Status: The game is over. You won!")
    elif status == 'com_w':
        print("Status: The game is over. The computer won!")


def com_step():
    global r_pie, status
    r_pie = choice(com_pie)
    snake.append(r_pie)
    com_pie.remove(r_pie)
    status = 'player'


def pla_step():
    global status, pla_in, r_pie
    if pla_in == 0:
        r_pie = choice(res)
        pla_pie.append(r_pie)
        res.remove(r_pie)
        status = 'computer'
    elif pla_in > 0:
        r_pie = pla_pie[pla_in-1]
        snake.append(r_pie)
        pla_pie.remove(r_pie)
        status = 'computer'
    elif pla_in < 0:
        pla_in = abs(pla_in)
        r_pie = pla_pie[pla_in - 1]
        snake.insert(0, r_pie)
        pla_pie.remove(r_pie)
        status = 'computer'


def draw():
    global status, dra
    for i in snake:
        for j in range(2):
            dra.append(i[j])
        for k in range(7):
            if dra.count(k) == 8:
                if dra[0] == dra[-1] == k:
                    status = 'draw'
    dra.clear()


def fin():
    global status
    if len(com_pie) == 0:
        status = 'com_w'
    elif len(pla_pie) == 0:
        status = 'pla_w'
    draw()


def result():
    print(70 * '=')
    print('Stock size: ' + str(len(res)))
    print('Computer pieces: ' + str(len(com_pie)) + '\n')
    snake_v()
    print('\n')
    print('Your pieces: ')
    fenshui()
    print('')
    fin()
    f_res()


def cho():
    while len(snake) == 0:
        res.clear()
        com_pie.clear()
        pla_pie.clear()
        he_ha()
        drop_all()
        arc()
    result()


cho()
while True:
    pla_in = input()
    if status == 'computer':
        com_step()
        result()
    elif status == 'player':
        pla_in = int(pla_in)
        if pla_in not in range(-len(pla_pie), len(pla_pie) + 1):
            print('Invalid input. Please try again.')
            continue
        else:
            pla_step()
            result()
    elif status != 'computer' or 'player':
        break

