from random import choice
d = {}
s = []
name = 0
all_amount = 0
answer = 0
r_name = 0
count = 0


def start():
    global name, all_amount, r_name, count
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count):
        name = input()
        d[name] = 0
        s.append(name)
    r_name = choice(s)
    print('Enter the total amount:')
    all_amount = int(input())
    for name in d:
        d[name] = round(all_amount / count, 2)


def lucky():
    global name, r_name
    for name in d:
        if name != r_name:
            d[name] = round(all_amount / (count - 1), 2)
        else:
            d[name] = 0
    print(d)


try:
    count = int(input('Enter the number of friends joining (including you):\n'))
    if count <= 0:
        print('No one is joining for the party')
    else:
        start()
        answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if answer == 'Yes':
            print(str(r_name) + ' is the lucky one!\n')
            lucky()
        else:
            print('No one is going to be lucky\n')
            print(d)
except ValueError:
    print('No one is joining for the party')
