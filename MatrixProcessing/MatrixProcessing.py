m_1 = m_2 = n_1 = n_2 = 0
b = c = d = []
e = []


def matrs():
    global m_1, m_2, n_1, n_2, b, c
    m_1, n_1 = input().split(' ')
    b = [[int(k) for k in input().split(' ')] for t in range(int(m_1))]
    m_2, n_2 = input().split(' ')
    c = [[int(k) for k in input().split(' ')] for t in range(int(m_2))]


def res():
    for i in range(int(m_1)):
        print(' '.join(map(str, d[i])))


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
            print("ERROR")
    else:
        print("ERROR")


def multiply_const():
    global m_1, n_1, b, e, d
    m_1, n_1 = input().split(' ')
    b = [[int(k) for k in input().split(' ')] for t in range(int(m_1))]
    cons = int(input())
    for i in range(int(m_1)):
        for j in range(int(n_1)):
            e.append(b[i][j] * cons)
        d.append(e)
        e = []
    res()


multiply_const()
