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


def result():
    print(res)
    print(com_pie)
    print(pla_pie)
    print(snake)
    print(status)


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
