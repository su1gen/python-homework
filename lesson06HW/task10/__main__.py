# Система управления персоналом. Это упражнение предполагает создание класса
# Employee из задачи 4 по программированию. Создайте программу, которая сохраняет
# объекты Employee в словаре. Используйте идентификационный номер сотрудника в качестве ключа.
# Программа должна вывести меню, которое позволяет пользователю:
# • найти сотрудника в словаре;
# • добавить нового сотрудника в словарь;
# • изменить имя, отдел и должность существующего сотрудника в словаре;
# • удалить сотрудника из словаря;
# • выйти из программы.
# По завершении работы программа должна законсервировать словарь и сохранить его
# в файле. При каждом запуске программы она должна попытаться загрузить законсервированный словарь из файла.
# Если файл не существует, то программа должна начать
# работу с пустого словаря.

from lesson06HW.task07.employee import Employee

import pickle


def get_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except:
        return {}


def write_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


if __name__ == '__main__':
    dct = get_data('dict.txt')

    print(dct)

    while True:
        print("*************MENU**************")
        print("1. найти сотрудника в словаре")
        print("2. добавить нового сотрудника в словарь")
        print("3. изменить имя, отдел и должность существующего сотрудника в словаре")
        print("4. удалить сотрудника из словаря")
        print("0. Выход")

        choice = input("Выберите пункт ")

        if choice == '0':
            write_data(dct, 'dict.txt')
            break
        elif choice == '1':
            id = input('Введите идентификационный номер ')
            if id in dct:
                print(dct[id])
            else:
                print('Такого номера нет в списке!')
        elif choice == '2':
            name = input('Введите имя ')
            id = input('Введите идентификационный номер ')
            department = input('Введите отдел ')
            position = input('Введите должность ')
            if id in dct:
                print('Такой номер уже есть в списке!')
            else:
                employee = Employee(name, id, department, position)
                dct[id] = employee
        elif choice == '3':
            id = input('Введите идентификационный номер ')
            if id not in dct:
                print('Такого имени нет в списке!')
            else:
                name = input('Введите имя ')
                department = input('Введите отдел ')
                position = input('Введите должность ')
                dct[id].set_name(name)
                dct[id].set_department(department)
                dct[id].set_position(position)
        elif choice == '4':
            id = input('Введите идентификационный номер ')
            if id not in dct:
                print('Такого имени нет в списке!')
            else:
                del dct[id]
