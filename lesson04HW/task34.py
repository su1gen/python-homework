# Конвертер азбуки Морзе. Азбука Морзе представляет собой кодировку, где каждая
# буква алфавита, каждая цифра и различные знаки препинания представлены серией точек
# и тире. В табл. 8.4 и 8.5 показана часть этой азбуки.
# Напишите программу, которая просит пользователя ввести строковое значение и затем
# преобразует это строковое значение в кодировку азбукой Морзе.

string = input('Enter text ')

morze = ''

for ch in string:
    if ch == ' ':
        morze += ' '
    elif ch == ',':
        morze += '--..--'
    elif ch == '.':
        morze += '.-.-.-'
    elif ch == '?':
        morze += '..--..'
    elif ch == '0':
        morze += '-----'
    elif ch == '1':
        morze += '.----'
    elif ch == '2':
        morze += '..---'
    elif ch == '3':
        morze += '...--'
    elif ch == '4':
        morze += '....-'
    elif ch == '5':
        morze += '.....'
    elif ch == '6':
        morze += '-....'
    elif ch == '7':
        morze += '--...'
    elif ch == '8':
        morze += '---..'
    elif ch == '9':
        morze += '----.'
    elif ch.upper() == 'A':
        morze += '.-'
    elif ch.upper() == 'B':
        morze += '-...'
    elif ch.upper() == 'C':
        morze += '-.-.'
    elif ch.upper() == 'D':
        morze += '-..'
    elif ch.upper() == 'E':
        morze += '.'
    elif ch.upper() == 'F':
        morze += '..-.'
    elif ch.upper() == 'G':
        morze += '--.'
    elif ch.upper() == 'H':
        morze += '....'
    elif ch.upper() == 'I':
        morze += '..'
    elif ch.upper() == 'J':
        morze += '.---'
    elif ch.upper() == 'K':
        morze += '-.-'
    elif ch.upper() == 'L':
        morze += '.-..'
    elif ch.upper() == 'M':
        morze += '--'
    elif ch.upper() == 'N':
        morze += '-.'
    elif ch.upper() == 'O':
        morze += '---'
    elif ch.upper() == 'P':
        morze += '.--.'
    elif ch.upper() == 'Q':
        morze += '--.-'
    elif ch.upper() == 'R':
        morze += '.-.'
    elif ch.upper() == 'S':
        morze += '...'
    elif ch.upper() == 'T':
        morze += '-'
    elif ch.upper() == 'U':
        morze += '..-'
    elif ch.upper() == 'V':
        morze += '...-'
    elif ch.upper() == 'W':
        morze += '.--'
    elif ch.upper() == 'X':
        morze += '-..-'
    elif ch.upper() == 'Y':
        morze += '-.-'
    elif ch.upper() == 'Z':
        morze += '--..'

print(morze)