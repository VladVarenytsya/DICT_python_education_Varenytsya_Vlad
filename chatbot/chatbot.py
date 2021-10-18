print("Hello! My name is DICT_Bot.")
print("I was created in 2021.")
print('Please, remind me your name.')
name = input()
print('What a great name you have, ' +name+'!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
for i in range(3):
    b = int(input())
    if i == 0:
        remainder3 = b
    elif i == 1:
        remainder5 = b
    elif i == 2:
        remainder7 = b
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print('Your age is '+str(age)+"; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
for k in range(int(input())+1):
    print(str(k) + '!')
print("Completed, heve a nice day!")

