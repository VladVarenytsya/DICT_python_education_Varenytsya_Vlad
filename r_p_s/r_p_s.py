import random

l = ['rock', 'paper', 'scissors']
s = [0] * len(l)
rad = len(l)//2
player_an = 0


def game_3():
    for g in range(1, len(l)):
        s[player_num] = 0
        if g <= rad:
            s[player_num - g] = 1
        elif g > rad:
            s[player_num - g] = -1
    if player_num - comp_num == 0:
        print(f'There is a draw ({comp_an})')
    elif s[comp_num] == -1:
        print(f'Sorry, but the computer chose {comp_an}')
    elif s[comp_num] == 1:
        print(f'Well done. The computer chose {comp_an} and failed')


def game():
    for g in range(1, len(l)):
        s[player_num] = 0
        if g < rad:
            s[player_num - g] = 1
        elif g >= rad:
            s[player_num - g] = -1
    if player_num - comp_num == 0:
        print(f'There is a draw ({comp_an})')
    elif s[comp_num] == -1:
        print(f'Sorry, but the computer chose {comp_an}')
    elif s[comp_num] == 1:
        print(f'Well done. The computer chose {comp_an} and failed')


while player_an != "!exit":
    try:
        player_an = input('Your action: > ')
        player_num = l.index(player_an)
        comp_an = random.choice(l)
        comp_num = l.index(comp_an)
    except ValueError:
        if player_an == '!exit':
            break
        print('Invalid input')
        continue
    if len(l) == 3:
        game_3()
    else:
        game()
print('Bye!')
