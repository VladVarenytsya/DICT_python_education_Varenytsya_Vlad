from math import ceil, log
print('Enter the loan principal:')
print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
choice = input()
if choice == 'n':
    print('Enter the loan principal:')
    p = float(input())
    print('Enter the monthly payment:')
    a = float(input())
    print('Enter the loan interest:')
    i = float(input()) / 1200
    n = ceil(log(a / (a - (i * p)), (1 + i)))
    if n // 12 == 0:
        print('It will take ' + str(n) + ' months to repay this loan!')
    elif n % 12 == 0:
        print('It will take ' + str(n // 12) + ' years to repay this loan!')
    elif n % 12 != 0:
        print('It will take ' + str(n // 12) + ' years and ' + str(n % 12) + ' months to repay this loan!')
elif choice == 'a':
    print('Enter the loan principal:')
    p = float(input())
    print('Enter the number of periods:')
    n = float(input())
    print('Enter the loan interest:')
    i = float(input()) / 1200
    i_n = (1 + i) ** n
    a = ceil(p * (i * i_n / (i_n - 1)))
    print('Your monthly payment = ' + str(a) + '!')
elif choice == 'p':
    print('Enter the annuity payment:')
    a = float(input())
    print('Enter the number of periods:')
    n = float(input())
    print('Enter the loan interest:')
    i = float(input()) / 1200
    i_n = (1 + i) ** n
    p = round(a / (i * i_n / (i_n - 1)))
    print('Your loan principal = ' + str(p) + '!')
