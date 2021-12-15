from random import choice
count = int(input('Enter the number of friends joining (including you):\n'))
d = {}
s = []
if count >= 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count):
        name = input()
        d[name] = 0
        s.append(name)
else:
    print('No one is joining for the party')
print('Enter the total amount:')
all_amount = int(input())
for name in d:
    d[name] = round(all_amount / count, 2)
r_name = choice(s)
answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if answer == 'Yes':
    print(r_name + ' is the lucky one!')
else:
    print('No one is going to be lucky')
