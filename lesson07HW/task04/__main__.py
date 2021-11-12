# Класс ShiftSupervisor. На некой фабрике начальник смены является штатным сотрудником,
# который руководит сменой. В дополнение к фиксированному окладу начальник
# смены получает годовую премию за выполнение его сменой производственного плана.
# Напишите класс ShiftSupervisor (Начальник смены), который является подклассом
# класса Ernployee, созданного в задаче по программированию 1. Класс ShiftSupervisor
# должен содержать атрибут данных для годового оклада и атрибут данных для годовой
# производственной премии, которую заработал начальник смены. Продемонстрируйте
# класс, написав программу, которая применяет объект ShiftSupervisor.
from lesson07HW.task04.shift_supervisor import ShiftSupervisor

if __name__ == '__main__':
    name = input('Enter name ')
    number = input('Enter number ')
    year_salary = float(input('Enter year salary '))
    year_prize = float(input('Enter year prize '))

    supervisor = ShiftSupervisor(name, number, year_salary, year_prize)

    print(supervisor)