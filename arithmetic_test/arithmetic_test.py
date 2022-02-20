from random import choice
res = 0
count = 0
mark = 0
status = 1
first_1 = 0
first_2 = 0
ar = 0
level = 0
second = 0


def lvl_1_p():
    global first_1, first_2, ar
    if status == 1:
        first_1 = choice(range(2, 10))
        first_2 = choice(range(2, 10))
        ar = choice(['+', '-', '*'])


def lvl_2():
    global second, res
    second = choice(range(11, 30))
    res = second ** 2
    print(second)


def lvl_1():
    global res, first_1, first_2, ar
    lvl_1_p()
    if ar == '+':
        print(str(first_1) + ' + ' + str(first_2))
        res = first_1 + first_2
    elif ar == '-':
        print(str(first_1) + ' - ' + str(first_2))
        res = first_1 - first_2
    elif ar == '*':
        print(str(first_1) + ' * ' + str(first_2))
        res = first_1 * first_2


def result():
    global mark, count, status
    if res == answer:
        print('Right!')
        mark += 1
        count += 1
        status = 1
    else:
        print('Wrong!')
        count += 1
        status = 1


while level not in [1, 2]:
    try:
        print("Which level do you want? Enter a number:")
        level = int(input())
    except ValueError:
        print("Incorrect format.")


while count != 5:
    try:
        if level == 1:
            lvl_1()
            answer = int(input())
            result()
        elif level == 2:
            lvl_2()
            answer = int(input())
            result()
    except ValueError:
        print('Incorrect format')
        status = 0
print('Your mark is ' + str(mark) + '/5')
print("Would you like to save the result? Enter yes or no.")
answer_file = input()
if answer_file == 'YES' or 'Yes' or 'y' or 'yes':
    name = input('What is your name? \n')
    file = open('results.txt', 'w')
    file.write(name + ':' + str(mark) + '/5 ' + 'in level ' + str(level) + '\n')
    file.close()
    print('The results are saved in "results.txt".')
