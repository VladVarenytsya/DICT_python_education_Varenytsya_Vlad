import math
print('Enter the loan principal:')
l_p = int(input()) # 1000
print('What do you want to calculate?\ntype "m" – for number of monthly payments,\ntype "p" – for the monthly payment:')
choice = input()
if choice == 'm':
    print('Enter the monthly payment:')
    m_p = int(input()) # 150
    print('It will take ' + str(math.ceil(l_p / m_p)) + ' months to repay the loan')
else:
    print('Enter the number of months:')
    n_m = int(input()) # 9
    p_m = math.ceil(l_p / n_m) # 112
    last_p = l_p - (n_m - 1) * p_m
    if last_p == p_m:
        print('Your monthly payment = ' + str(p_m))
    else:
        print('Your monthly payment = ' + str(p_m) + ' and the last payment = ' + str(last_p))
