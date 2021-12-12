from math import ceil
m_1 = m_2 = n_1 = n_2 = s = cons = 0
b = c = []
d = []
e = []
answer = 9


def matrs():
    global m_1, m_2, n_1, n_2, b, c
    print('Enter size of first matrix: ')
    m_1, n_1 = input().split(' ')
    m_1 = int(m_1)
    n_1 = int(n_1)
    print('Enter first matrix:')
    b = [[float(k) for k in input().split(' ')] for _ in range(int(m_1))]
    print('Enter size of second matrix: ')
    m_2, n_2 = input().split(' ')
    m_2 = int(m_1)
    n_2 = int(n_2)
    print('Enter second matrix:')       
    c = [[float(k) for k in input().split(' ')] for _ in range(int(m_2))]


def matr():
    global m_1, n_1, b
    print('Enter size of matrix: ')
    m_1, n_1 = input().split(' ')
    m_1 = int(m_1)
    n_1 = int(n_1)
    print('Enter matrix:')
    b = [[int(k) for k in input().split(' ')] for _ in range(m_1)]


def res():
    global d
    print('The result is:')
    for i in range(m_1):
        print(' '.join(map(str, d[i])))
    d = []


def res_s():
    global b
    print('The result is:')
    for i in range(m_1):
        print(' '.join(map(str, b[i])))
    b = []


def sum():
    global d, e
    matrs()
    if m_1 == m_2:
        if n_1 == n_2:
            for i in range(m_1):
                for j in range(n_1):
                    e.append(b[i][j] + c[i][j])
                d.append(e)
                e = []
            res()
        else:
            print("The operation cannot be performed.")
    else:
        print("The operation cannot be performed.")


def multiply_const(bdf):
    global e, d, cons
    for i in range(m_1):
        for j in range(n_1):
            e.append(round(bdf[i][j] * cons, 2))
        d.append(e)
        e = []
    return d


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
    l = m_1 - 1
    f = ceil(l / 2)
    for i in range(f):
        for j in range(l+1):
            b[i][j], b[l - i][j] = b[l - i][j], b[i][j]
    res_s()


def t_matrix_vert():
    global m_1, n_1, b
    matr()
    l = m_1 - 1
    f = ceil(l / 2)
    for i in range(l+1):
        for j in range(f):
            b[i][j], b[i][l - j] = b[i][l - j], b[i][j]
    res_s()


def t_matrix_main(bld):
    global m_1, n_1
    for i in range(m_1):
        for j in range(m_1):
            if i > j:
                bld[i][j], bld[j][i] = bld[j][i], bld[i][j]
    return bld


def t_matrix_side():
    global m_1, n_1, b
    matr()
    l = m_1 - 1
    for i in range(l+1):
        for j in range(l+1):
            if i > l - j:
                b[i][j], b[l - j][l - i] = b[l - j][l - i], b[i][j]
    res_s()


def transpose_matrix():
    print('1.Main diagonal\n2.Side diagonal\n3.Vertical line\n4.Horizontal line\nYour choice: ')
    choice = int(input())
    if choice == 1:
        matr()
        t_matrix_main(b)
    elif choice == 2:
        t_matrix_side()
    elif choice == 3:
        t_matrix_vert()
    elif choice == 4:
        t_matrix_hor()
    else:
        print('The operation cannot be performed.')


def minor(l, i_1, j_1):
    return [k[:j_1] + k[j_1 + 1:] for k in (l[:i_1] + l[i_1 + 1:])]


def determinant(l):
    if len(l) == 2:
        return l[0][0] * l[1][1] - l[0][1] * l[1][0]
    dete = 0
    for j in range(len(l)):
        dete += ((-1) ** j) * l[0][j] * determinant(minor(l, 0, j))
    return dete


def invite(k):
    global cons, d
    for i in range(m_1):
        for j in range(n_1):
            if i+j % 2 == 0:
                b_1[i][j] = determinant(minor(k, i, j))
            else:
                b_1[i][j] = -(determinant(minor(k, i, j)))
    try:
        cons = 1 / determinant(k)
        cad = multiply_const(t_matrix_main(b_1))
        for z in range(m_1):
            print(' '.join(map(str, cad[z])))
    except ZeroDivisionError:
        print("This matrix doesn't have an inverse.")


while answer != 0:

    print('1.Add matrices\n2.Multiply matrix by a constant\n3.Multiply matrices')
    print('4.Transpose matrix\n5.Calculate a determinant\n6.Inverse matrix\n0.Exit\nYour choice:')
    answer = int(input())
    if answer == 0:
        break
    elif answer == 1:
        sum()
    elif answer == 2:
        print('Enter size of matrix: ')
        m_1, n_1 = input().split(' ')
        print('Enter matrix:')
        b = [[float(k) for k in input().split(' ')] for _ in range(int(m_1))]
        print('Enter constant: ')
        cons = float(input())
        multiply_const(b)
    elif answer == 3:
        multiply_matrix()
    elif answer == 4:
        transpose_matrix()
    elif answer == 5:
        matr()
        print('The result is:\n' + str(determinant(b)))
    elif answer == 6:
        matr()
        b_1 = [['_' for k in range(m_1)] for v in range(n_1)]
        print('The result is:')
        invite(b)
        print()
