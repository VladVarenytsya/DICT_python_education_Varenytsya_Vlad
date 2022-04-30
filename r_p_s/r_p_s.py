import random

player_an = 0
result = 0
rate = 0
user = input('Enter your name: > ')
print(f'Hello, {user}')
p = input()
if p == '':
    p = ['rock', 'paper', 'scissors']
else:
    p = p.split(',')
print("Okay, let's start")
s = [0] * len(p)
rad = len(p)//2
f = open('rating.txt')
for i in f:
    if user in i:
        a, rate = i.split(' ')
        rate = int(rate[:-1])
        break
f.close()


def answer():
    global result
    if player_num - comp_num == 0:
        print(f'There is a draw ({comp_an})')
        result = 'Draw'
    elif s[comp_num] == -1:
        print(f'Sorry, but the computer chose {comp_an}')
        result = 'Lose'
    elif s[comp_num] == 1:
        print(f'Well done. The computer chose {comp_an} and failed')
        result = 'Win'
    res()


def game_3():
    for g in range(1, len(p)):
        s[player_num] = 0
        if g <= rad:
            s[player_num - g] = 1
        elif g > rad:
            s[player_num - g] = -1
    answer()


def game():
    for g in range(1, len(p)):
        s[player_num] = 0
        if g <= rad:
            s[player_num - g] = 1
        elif g > rad:
            s[player_num - g] = -1
    answer()


def res():
    global rate
    if result == 'Win':
        rate += 100
    elif result == 'Draw':
        rate += 50

# def rating():
    # f = open('rating.txt', 'a')
    # f.write(user)
    # f.close()


while player_an != "!exit":
    try:
        player_an = input('Your action: > ')
        if player_an == '!rating':
            print(f'Your rating: {rate}')
            continue
        player_num = p.index(player_an)
        comp_an = random.choice(p)
        comp_num = p.index(comp_an)
    except ValueError:
        if player_an == '!exit':
            break
        print('Invalid input')
        continue
    if len(p) == 3:
        game_3()
    else:
        game()
print('Bye!')
