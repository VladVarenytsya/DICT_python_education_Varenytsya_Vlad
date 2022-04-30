from random import choice

com_pie = []
pla_pie = []
res = []
snake = []
status = 0
r_pie = []
pla_in = 0
dra = []
snake_2 = []
sn_up = 0
sn_down = 0
comp_d = {i: 0 for i in range(7)}
comp_d_2 = []
com_status = 2
com_pie_2 = []
comp_cont = 'no'


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


def true_snake():
    global sn_down, sn_up
    snake_2.clear()
    for i in snake:
        snake_2.append(i[0])
        snake_2.append(i[1])
    sn_up = snake_2[0]
    sn_down = snake_2[-1]


def comp_ch():
    global com_pie_2, comp_d
    true_snake()
    comp_d = {i: 0 for i in range(7)}
    for k in com_pie:
        comp_d_2.append(k[0])
        comp_d_2.append(k[1])
    for i in range(7):
        comp_d[i] = snake_2.count(i) + comp_d_2.count(i)
    comp_d_2.clear()
    com_pie_2 = com_pie.copy()


def comp_ch_2():
    global com_pie_2, r_pie
    if len(comp_d_2) == 0:
        for k in com_pie_2:
            sat = comp_d.get(k[0]) + comp_d.get(k[1])
            comp_d_2.append(sat)
    for i in com_pie_2:
        sat = comp_d.get(i[0]) + comp_d.get(i[1])
        if sat == max(comp_d_2):
            comp_d_2.remove(sat)
            com_pie_2.remove(i)
            r_pie = i
            break


def comp_ch_3():
    global com_status, comp_cont
    if sn_up in r_pie:
        if r_pie[1] == sn_up:
            com_status = -1
            comp_cont = 'yes'
        else:
            r_pie.reverse()
            com_status = -1
            comp_cont = 'yes'
    elif sn_down in r_pie:
        if r_pie[0] == sn_down:
            com_status = 1
            comp_cont = 'yes'
        else:
            r_pie.reverse()
            com_status = 1
            comp_cont = 'yes'
    else:
        if len(comp_d_2) == 1:
            com_status = 0
            comp_cont = 'yes'


def com_step():
    global r_pie, status
    comp_ch_3()
    if com_status == 1:
        snake.append(r_pie)
        com_pie.remove(r_pie)
        status = 'player'
    elif com_status == -1:
        snake.insert(0, r_pie)
        com_pie.remove(r_pie)
        status = 'player'
    elif com_status == 0:
        com_pie.append(choice(res))
        status = 'player'


def play_in_up():
    global r_pie, status, sn_up, pla_in
    true_snake()
    pla_in = abs(pla_in)
    r_pie = pla_pie[pla_in - 1]
    if sn_up in r_pie:
        if sn_up == r_pie[1]:
            snake.insert(0, r_pie)
            pla_pie.remove(r_pie)
            status = 'computer'
        else:
            r_pie.reverse()
            snake.insert(0, r_pie)
            pla_pie.remove(r_pie)
            status = 'computer'
    else:
        print('Illegal move. Please try again.')


def play_in_down():
    global r_pie, status, sn_down
    true_snake()
    r_pie = pla_pie[pla_in - 1]
    if sn_down in r_pie:
        if sn_down == r_pie[0]:
            snake.append(r_pie)
            pla_pie.remove(r_pie)
            status = 'computer'
        else:
            r_pie.reverse()
            snake.append(r_pie)
            pla_pie.remove(r_pie)
            status = 'computer'
    else:
        print('Illegal move. Please try again.')


def pla_step():
    global status, pla_in, r_pie
    if pla_in == 0:
        r_pie = choice(res)
        pla_pie.append(r_pie)
        res.remove(r_pie)
        status = 'computer'
    elif pla_in > 0:
        play_in_down()
    elif pla_in < 0:
        play_in_up()


def draw():
    global status, dra
    for i in snake:
        dra.append(i[0])
        dra.append(i[1])
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
        comp_ch()
        while comp_cont == 'no':
            comp_ch_2()
            comp_ch_3()
        com_step()
        result()
        comp_cont = 'no'
    elif status == 'player':
        try:
            pla_in = int(pla_in)
        except ValueError:
            print('Invalid input. Please try again.')
            continue
        if pla_in not in range(-len(pla_pie), len(pla_pie) + 1):
            print('Invalid input. Please try again.')
            continue
        else:
            pla_step()
            result()
    elif status != 'computer' or 'player':
        break
