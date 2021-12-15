print('Enter the number of friends joining (including you):')
count = int(input())
d = {}
if count >= 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count):
        name = input()
        d[name] = 0
else:
    print('No one is joining for the party')
print('Enter the total amount:')
all_amount = int(input())
amount = round(all_amount / count, 2)
for name in d:
    d[name] = amount
print(d)
