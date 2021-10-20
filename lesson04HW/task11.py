# Номера строк. Напишите программу, которая запрашивает у пользователя имя файла.
# Программа должна вывести на экран содержимое файла, при этом каждая строка должна
# предваряться ее номером и двоеточием. Нумерация строк должна начинаться с 1.


file_name = input('Enter file name ')

try:
    with open(file_name, 'r', encoding='utf8') as file:
        key = 1
        for line in file:
            print(f'{key}: {line.rstrip()}')
            key += 1
except FileNotFoundError:
    print('This file does not exists')