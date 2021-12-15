print('Enter the number of friends joining (including you):')
count = int(input())
d = {}
if count >= 0:
    for i in range(count):
        print('Enter the name of every friend (including you), each on a new line:')
        name = input()
        d[name] = 0
else:
    print('No one is joining for the party')
print(d)
