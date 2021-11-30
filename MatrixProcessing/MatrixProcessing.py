from math import ceil
m_1 = m_2 = n_1 = n_2 = s = 0
b = c = []
d = []
e = []
answer = 9


def matrs():
    global m_1, m_2, n_1, n_2, b, c
    print('Enter size of first matrix: ')
    m_1, n_1 = input().split(' ')
    print('Enter first matrix:')
    b = [[int(k) for k in input().split(' ')] for _ in range(int(m_1))]
    print('Enter size of second matrix: ')
    m_2, n_2 = input().split(' ')
    print('Enter second matrix:')       
    c = [[int(k) for k in input().split(' ')] for _ in range(int(m_2))]


def matr():
    global m_1, n_1, b, e, d
    print('Enter size of matrix: ')
    m_1, n_1 = input().split(' ')
    print('Enter matrix:')
    b = [[int(k) for k in input().split(' ')] for _ in range(int(m_1))]


def res():
    global d
    print('The result is:')
    for i in range(int(m_1)):
        print(' '.join(map(str, d[i])))
    d = []


def res_s():
    global b
    print('The result is:')
    for i in range(int(m_1)):
        print(' '.join(map(str, (b[i]))))
    b = []


def sum():
    global d, e
    matrs()
    if m_1 == m_2:
        if n_1 == n_2:
            for i in range(int(m_1)):
                for j in range(int(n_1)):
                    e.append(b[i][j] + c[i][j])
                d.append(e)
                e = []
            res()
        else:
            print("The operation cannot be performed.")
    else:
        print("The operation cannot be performed.")


def multiply_const():
    global m_1, n_1, b, e, d
    print('Enter size of matrix: ')
    m_1, n_1 = input().split(' ')
    print('Enter matrix:')
    b = [[float(k) for k in input().split(' ')] for _ in range(int(m_1))]
    print('Enter constant: ')
    cons = float(input())
    for i in range(int(m_1)):
        for j in range(int(n_1)):
            e.append(b[i][j] * cons)
        d.append(e)
        e = []
    res()


def multiply_matrix():
    global m_1, m_2, n_1, n_2, b, c, s, e, d
    matrs()
    if int(m_1) == int(n_2):
        for k in range(int(m_1)):
            for i in range(int(n_2)):
                for j in range(int(m_2)):
                    s += b[k][j] * c[j][i]
                e.append(s)
                s = 0
            d.append(e)
            e = []
        res()
    else:
        print('The operation cannot be performed.')


def t_matrix_hor():
    global m_1, n_1, b
    matr()
    l = int(m_1) - 1
    f = ceil(l / 2)
    for i in range(f):
        for j in range(l+1):
            b[i][j], b[l - i][j] = b[l - i][j], b[i][j]
    res_s()


def t_matrix_vert():
    global m_1, n_1, b
    matr()
    l = int(m_1) - 1
    f = ceil(l / 2)
    for i in range(l+1):
        for j in range(f):
            b[i][j], b[i][l - j] = b[i][l - j], b[i][j]
    res_s()


def t_matrix_main():
    global m_1, n_1, b
    matr()
    l = int(m_1)
    for i in range(l):
        for j in range(l):
            if i > j:
                b[i][j], b[j][i] = b[j][i], b[i][j]
    res_s()


def t_matrix_side():
    global m_1, n_1, b
    matr()
    l = int(m_1) - 1
    for i in range(l+1):
        for j in range(l+1):
            if i > l - j:
                b[i][j], b[l - j][l - i] = b[l - j][l - i], b[i][j]
    res_s()


def transpose_matrix():
    print('1.Main diagonal\n2.Side diagonal\n3.Vertical line\n4.Horizontal line\nYour choice: ')
    choice = int(input())
    if choice == 1:
        t_matrix_main()
    elif choice == 2:
        t_matrix_side()
    elif choice == 3:
        t_matrix_vert()
    elif choice == 4:
        t_matrix_hor()
    else:
        print('The operation cannot be performed.')


while answer != 0:
    print('1.Add matrices\n2.Multiply matrix by a constant\n3.Multiply matrices\n4.Transpose matrix\n0.Exit\nYour choice:')
    answer = int(input())
    if answer == 0:
        break
    elif answer == 1:
        sum()
    elif answer == 2:
        multiply_const()
    elif answer == 3:
        multiply_matrix()
    elif answer == 4:
        transpose_matrix()
