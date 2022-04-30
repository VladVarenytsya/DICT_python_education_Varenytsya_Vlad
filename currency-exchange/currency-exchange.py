import requests
import json


cache_user = {}
dict_json = {}
user_input = input()
user_input_1 = 0


def req():
    global dict_json
    dict_0 = requests.get('http://www.floatrates.com/daily/' + user_input + '.json')
    with open('another.json', 'w') as file:
        json.dump(dict_0.json(), file)
    with open('another.json', 'r') as file:
        for line in file:
            string = line
        dict_json = json.loads(string)


def cache_write():
    with open('cache.txt', 'w') as file:
        for key, values in cache_user.items():
            file.write(f'{key},{values},\n')


def cache_read():
    try:
        with open('cache.txt', 'r') as file:
            for line in file:
                key, values, trash = line.split(',')
                cache_user[key] = values
    except ValueError:
        ...


cache_read()
while True:
    user_input_1 = input()
    if user_input_1 == '':
        cache_write()
        break
    count_money = int(input())
    pair = (user_input + '-' + user_input_1)
    r_pair = (user_input_1 + '-' + user_input)
    print('Checking the cache... ')
    try:
        if pair in cache_user:
            print('It is in the cache!')
            rate = float(cache_user[pair])
        elif r_pair in cache_user:
            print('It is in the cache!')
            rate = round(1 / float(cache_user[r_pair]), 2)
        else:
            print('Sorry, but it is not in the cache!')
            if dict_json == {}:
                req()
                rate = round(float(dict_json[user_input_1]['rate']), 2)
                cache_user[pair] = rate
            else:
                rate = round(float(dict_json[user_input_1]['rate']), 2)
                cache_user[pair] = rate
    except KeyError:
        print('Invalid input. Try again')
        continue
    print('You received ' + str(rate * count_money) + ' ' + str(user_input_1))



