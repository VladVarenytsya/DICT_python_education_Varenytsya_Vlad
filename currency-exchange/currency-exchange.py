my_coin = float(input("Please, enter the number of mycoins you have: > "))
d = {'USD': 29.8, 'EUR': 33.3, 'PLN': 7, 'GBP': 40}
for i in d:
    index = i
    total = d[i] * my_coin
    print(f'I will get {round(total, 1)} {index} from the sale of {my_coin} mycoins')
