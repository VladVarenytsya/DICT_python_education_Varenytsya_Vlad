def hi():
    print("Hello! My name is DICT_Bot.")
    print("I was created in 2021.")
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' +name+'!')


def age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print('Your age is '+str(age)+"; that's a good time to start programming!")


def quest():
    print('Now I will prove to you that I can count to any number you want.')
    for k in range(int(input())+1):
        print(str(k) + '!')
    print("Completed, have a nice day!")
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    c = 0
    while c != 2:
        c = int(input())
        if c == 2:
            print("Congratulations, have a nice day!")
        else:
            print("Please, try again.")

hi()
age()
quest()
