import random
print("HANGMAN")
print("The game will be available soon.")
list_words = ['python', 'javascript', 'php', 'java']
answer_prog = random.choice(list_words)
print("Guess the word:")
answer_user = input()
if answer_user == answer_prog:
    print("You survived!")
else:
    print("You lost!")

