inp = 0
formats = 'Available formatters: plain, bold, italic, header, link, inline-code, ordered-list, unordered-list, new-line'
s_commands = 'Special commands: !help !done'
text = 0
text_2 = ''


def hellp():
    print(formats)
    print(s_commands)


def plain():
    global text_2
    text_2 += input('Text: > ')


def bold():
    global text, text_2
    text = input('Text: > ')
    text_2 += '**' + text + '**'


def italic():
    global text, text_2
    text = input('Text: > ')
    text_2 += '*' + text + '*'


def header():
    global text, text_2
    try:
        level = int(input('Level: > '))
        if level not in range(1, 7):
            print('The level should be within the range of 1 to 6. Try again')
            header()
        else:
            text = input('Text: > ')
            text_2 += '#' * level + ' ' + text + '\n'
    except ValueError:
        print('The level should be within the range of 1 to 6. Try again')
        header()


def link():
    global text_2
    label = input('Label: > ')
    url = input('URL: > ')
    text_2 += '\n' + '[' + label + ']' + '(' + url + ')' + '\n'


def inline_code():
    global text_2
    text_2 += '\n' + '~' + str(input('Enter your code: > ')) + '~' + '\n'


def ordered_list():
    global text_2
    try:
        nof = int(input('Number of rows: > '))
        if nof > 0:
            for i in range(1, nof + 1):
                row = str(input('Row #' + str(i) + ': > '))
                text_2 += str(i) + '. ' + row + '\n'
        else:
            print('The number of rows should be greater than zero')
            ordered_list()
    except ValueError:
        print('The number of rows should be greater than zero')
        ordered_list()


def unordered_list():
    global text_2
    try:
        nof = int(input('Number of rows: > '))
        if nof > 0:
            for i in range(1, nof + 1):
                row = str(input('Row #' + str(i) + ': > '))
                text_2 += '* ' + row + '\n'
        else:
            print('The number of rows should be greater than zero')
            unordered_list()
    except ValueError:
        print('The number of rows should be greater than zero')
        unordered_list()


def new_line():
    global text_2
    text_2 += '\n'


def space():
    global text_2
    text_2 += ' '


def all_func():
    global inp
    if inp == '':
        space()
    elif inp == 'plain':
        plain()
    elif inp == 'bold':
        bold()
    elif inp == 'italic':
        italic()
    elif inp == 'header':
        header()
    elif inp == 'link':
        link()
    elif inp == 'inline-code':
        inline_code()
    elif inp == 'ordered-list':
        ordered_list()
    elif inp == 'unordered-list':
        unordered_list()
    elif inp == 'new-line':
        new_line()
    else:
        print('Unknown formatting type or command')


while inp != '!done':
    inp = input('Choose a formatter: > ')
    if inp == '!help':
        hellp()
    elif inp == '!done':
        break
    else:
        all_func()
        print(text_2)
text_3 = open('output.md', 'w')
text_3.write(text_2)
text_3.close()


