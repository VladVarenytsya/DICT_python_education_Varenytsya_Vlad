import requests
import json


# cache_user = {}
# cache_user_write = {}
# cache_user_read = {}
dict_2 = {}
user_input = input()
user_input_1 = 0


def req():
    global dict_2
    dict_1 = requests.get('http://www.floatrates.com/daily/' + user_input + '.json')
    with open('another.json', 'w') as file:
        json.dump(dict_1.json(), file)
    with open('another.json', 'r') as file:
        for line in file:
            string = line
        dict_2 = json.loads(string)


# def cache_write():
#     with open('cache.txt', 'w') as file:
#         for key, values in cache_user_write.items():
#             file.write(f'{key},{values},\n')
#
#
# def cache_read():
#     with open('cache.txt', 'r') as file:
#         for line in file:
#             key, values, trash = line.split(',')
#             cache_user_read[key] = values


req()
while True:
    user_input_1 = input()
    if user_input_1 == '':
        break
    rate = dict_2[user_input_1]['rate']
    # cache_user[user_input] = rate
    count_money = float(input())
    print(str(round(count_money * rate, 2)) + ' ' + user_input_1)

