# Имена и адреса электронной почты. Напишите программу, которая сохраняет имена и
# адреса электронной почты в словаре в виде пар ключ/значение. Программа должна вывести меню,
# которое позволяет пользователю отыскать адрес электронной почты человека,
# добавить новое имя и адрес электронной почты, изменить существующий адрес электронной
# почты и удалить существующее имя и адрес электронной почты. Программа
# должна законсервировать словарь и сохранить его в файле при выходе пользователя из
# программы. При каждом запуске программы она должна извлечь словарь из файла и его
# расконсервировать.

import json

def get_data(filename):
    with open(filename, 'r', encoding='utf8') as file:
        try:
            return json.load(file)
        except:
            return {}


def write_data(data, filename):
    with open(filename, 'w', encoding='utf8') as file:
        return json.dump(data, file)


if __name__ == '__main__':
    dct = get_data('dict.txt')

    while True:
        print("*************MENU**************")
        print("1. Найти электронную почту по имени")
        print("2. Добавить новое имя и адрес электронной почты")
        print("3. Изменить существующий адрес электронной почты")
        print("4. Удалить существующее имя и адрес электронной почты")
        print("0. Выход")

        choice = input("Выберите пункт ")

        if choice == '0':
            write_data(dct, 'dict.txt')
            break
        elif choice == '1':
            name = input('Введите имя ')
            if name in dct:
                print(dct[name])
            else:
                print('Такого имени нет в списке!')
        elif choice == '2':
            name = input('Введите имя ')
            email = input('Введите электронную почту ')
            if name in dct:
                print('Такое имя уже есть в списке!')
            else:
                dct[name] = email
        elif choice == '3':
            name = input('Введите имя ')
            if name not in dct:
                print('Такого имени нет в списке!')
            else:
                email = input('Введите электронную почту ')
                dct[name] = email
        elif choice == '4':
            name = input('Введите имя ')
            if name not in dct:
                print('Такого имени нет в списке!')
            else:
                del dct[name]