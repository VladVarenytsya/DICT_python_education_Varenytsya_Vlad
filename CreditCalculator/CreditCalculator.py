from math import ceil, log, floor
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()
typ = args.type
principal = args.principal
period = args.periods
interest = args.interest / 1200
payment = args.payment


def F_diff_payment():
    i = 0
    sum_d_p = 0
    global payment, interest, period, principal, typ
    for k in range(1, period + 1):
        i += 1
        diff_payment = ceil(float(principal / period) + interest * (principal - principal * (k - 1) / period))
        print('Month ' + str(i) + ': payment is ' + str(int(diff_payment)))
        sum_d_p += diff_payment
    over = sum_d_p - principal
    print('Overpayment = ' + str(over))


def F_period():
    global payment, interest, period, principal, typ
    period = ceil(log(payment / (payment - (interest * principal)), (1 + interest)))
    if period // 12 == 0:
        print('It will take ' + str(period) + ' months to repay this loan!')
    elif period % 12 == 0:
        print('It will take ' + str(period // 12) + ' years to repay this loan!')
    elif period % 12 != 0:
        print('It will take ' + str(period // 12) + ' years and ' + str(period % 12) + ' months to repay this loan!')
    over = payment * period - principal
    print('Overpayment = ' + str(over))


def F_payment():
    global payment, interest, period, principal, typ
    i_period = (1 + interest) ** period
    payment = ceil(principal * (interest * i_period / (i_period - 1)))
    print('Your monthly payment = ' + str(payment) + '!')
    over = payment * period - principal
    print('Overpayment = ' + str(over))


def F_principal():
    global payment, interest, period, principal, typ
    i_period = (1 + interest) ** period
    principal = floor(payment / (interest * i_period / (i_period - 1)))
    print('Your loan principal = ' + str(principal) + '!')
    over = payment * period - principal
    print('Overpayment = ' + str(over))

try:
    if typ == "annuity":
        if period is None:
            if principal > 0 and payment > 0 and interest > 0:
                F_period()
            else:
                print("Incorrect parameters")
        elif payment is None:
            if principal > 0 and period > 0 and interest > 0:
                F_payment()
            else:
                print("Incorrect parameters")
        elif principal is None:
            if payment > 0 and period > 0 and interest > 0:
                F_principal()
            else:
                print("Incorrect parameters")
    elif typ == "diff":
        if principal > 0 and period > 0 and interest > 0:
            F_diff_payment()
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
except TypeError:
    print("Incorrect parameters")


#python CreditCalculator\CreditCalculator.py --type=diff --principal=1000000 --periods=10 --interest=10
#python CreditCalculator\CreditCalculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
#python CreditCalculator\CreditCalculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
#python CreditCalculator\CreditCalculator.py --type=annuity --principal=1000000 --periods=60 --interest=10