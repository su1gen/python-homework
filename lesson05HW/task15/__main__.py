# Шифрование и дешифрование файлов. Напишите программу, которая применяет словарь для присвоения "кодов"
# каждой букве алфавита. Например:
# codes = { , А, : , % , , , а, : , 9 ,, , Б, : , @,, , 6 , : , #, ... }
# Здесь букве А присвоен символ %, букве а - число 9, букве Б - символ @ и т. д. Программа должна открыть
# заданный текстовый файл, прочитать его содержимое и применить словарь для записи зашифрованной
# версии содержимого файла во второй файл.
# Каждый символ во втором файле должен содержать код для соответствующего символа
# из первого файла.
# Напишите вторую программу, которая открывает зашифрованный файл и показывает его
# дешифрованное содержимое на экране.


def encode(file_for_read, file_for_write):
    encoded_text = ''

    with open(file_for_read, 'r', encoding='utf8') as file:
        text = file.read()

    for ch in text:
        if ch in characters:
            encoded_text += str(characters[ch.lower()])
        else:
            encoded_text += ch

    with open(file_for_write, 'w', encoding='utf8') as file:
        file.write(encoded_text)


def decode(filename):

    decoded_text = ''
    characters_for_decode = {}

    for key, value in characters.items():
        characters_for_decode[value] = key

    with open(filename, 'r', encoding='utf8') as file:
        text = file.read()

    for ch in text:
        if ch in characters_for_decode:
            decoded_text += characters_for_decode[ch.lower()]
        else:
            decoded_text += ch

    return decoded_text


characters = {
    'a': '0',
    'b': '1',
    'c': '2',
    'd': '3',
    'e': '4',
    'f': '5',
    'g': '6',
    'h': '7',
    'i': '8',
    'j': '9',
    'k': '!',
    'l': '@',
    'm': '#',
    'n': '$',
    'o': '%',
    'p': '^',
    'q': '&',
    'r': '(',
    's': ')',
    't': '-',
    'u': '_',
    'v': '=',
    'w': '+',
    'x': '*',
    'y': '/',
    'z': ':',
    '\n': ';',
    ' ': '{',
}

encode('text.txt', 'encoded.txt')

print(decode('encoded.txt'))