# Класс Employee. Напишите класс под названием Employee, который в атрибутах содержит
# данные о сотруднике: имя, идентификационный номер, отдел и должность.
# После написания данного класса напишите программу, которая создает три объекта
# Employee с приведенными в табл. 10.1 данными.
# Программа должна сохранить эти данные в трех объектах и затем вывести данные по
# каждому сотруднику на экран.

from lesson06HW.task07.employee import Employee

if __name__ == '__main__':
    employee1 = Employee('Сьюзан Мейерс', 47899, 'Бухгалтерия', 'Вице-президент')
    employee2 = Employee('МаркДжоунс', 39119, 'ит', 'Программист')
    employee3 = Employee('Джой Роджерс', 81774, 'Производственный', 'Инженер')

    print(employee1)
    print(employee2)
    print(employee3)