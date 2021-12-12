import random
print("HANGMAN")
print("The game will be available soon.")
words = ['python', 'javascript', 'html', 'java']
english_letters = list("qwertyuiopasdfghjklzxcvbnm")
answer_prog = random.choice(words)  # python
word_list = list(answer_prog) # [p,y,t,h,o,n]
user_word_list_null = "-" * len(answer_prog)    # ------
user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
user_used = []
start = 'play'
count = 0


def res():
    global start, user_list, word_list
    if user_list != word_list:
        print("You lost!")
    else:
        print("You guessed the word!")
        print("You survived!")
    start = str(input('Type "play" to play the game, "exit" to quit:'))


def double():
    global word_list, answer_user, user_list
    if word_list.count(answer_user) >= 2:
        index = word_list.index(answer_user)
        user_list[index] = answer_user
        word_list[index] = '-'


def exam():
    global count, answer_user, user_list, user_used, word_list
    if answer_user in user_used:
        print("You've already guessed this letter")
        count -= 1
    elif answer_user in word_list:
        double()
        index = word_list.index(answer_user)
        user_list[index] = answer_user
        count -= 1
    elif answer_user not in english_letters:
        print("Please enter a lowercase English letter")
        count -= 1
    elif len(answer_user) >= 2:
        print("You should input a single letter")
        count -= 1
    elif answer_user not in (user_used and word_list):
        print("That letter doesn't appear in the word")
    else:
        user_used.append(answer_user)


while start != 'exit':
    if start == "play":
        count = 0
        answer_prog = random.choice(words)  # python
        word_list = list(answer_prog)  # [p,y,t,h,o,n]
        user_word_list_null = "-" * len(answer_prog)  # ------
        user_used = []    # [-,-,-,-,-,-]
        user_list = list(user_word_list_null)
        print(user_word_list_null)
        while count != 8:
            answer_user = str(input('Input a letter:'))
            exam()
            count += 1
            print(''.join(user_list))
        word_list = list(answer_prog)
        res()
    start = str(input('Type "play" to play the game, "exit" to quit: '))

