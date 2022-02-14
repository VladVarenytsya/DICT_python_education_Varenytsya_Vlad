from random import choice
res = 0
count = 0
mark = 0
status = 1
first_1 = 0
second_1 = 0
ar = 0


def f_lvl_p():
    global first_1, second_1, ar
    if status == 1:
        first_1 = choice(range(2, 10))
        second_1 = choice(range(2, 10))
        ar = choice(['+', '-', '*'])


def f_lvl():
    global res, first_1, second_1, ar
    f_lvl_p()
    if ar == '+':
        print(str(first_1) + ' + ' + str(second_1))
        res = first_1 + second_1
    elif ar == '-':
        print(str(first_1) + ' - ' + str(second_1))
        res = first_1 - second_1
    elif ar == '*':
        print(str(first_1) + ' * ' + str(second_1))
        res = first_1 * second_1


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


while count != 5:
    try:
        f_lvl()
        answer = int(input())
        result()
    except ValueError:
        print('Incorrect format')
        status = 0
print('Your mark is ' + str(mark) + '/5')
