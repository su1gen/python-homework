# Магический квадрат Ло Шу. Магический квадрат Ло Шу представляет собой таблицу
# с 3 строками и 3 столбцами (рис. 7 .18). Магический квадрат Ло Шу имеет приведенные
# ниже свойства:
# • таблица содержит числа строго от 1 до 9;
# • сумма каждой строки, каждого столбца и каждой диагонали в итоге составляет одно
# и то же число (рис. 7 .19).
# Магический квадрат можно сымитировать в программе при помощи двумерного списка.
# Напишите функцию, которая принимает двумерный список в качестве аргумента и
# определяет, не является ли список магическим квадратом Ло Шу. Протестируйте функцию в программе.


def is_magic(array):
    summa = sum(array[0])
    for i in range(1, len(array)):
        line_summa = 0
        for j in array[i]:
            line_summa += j
        if line_summa != summa:
            return False

    line_summa = 0
    for i in range(len(array)):
        line_summa += array[i][i]
    if line_summa != summa:
        return False

    line_summa = 0
    for i in range(len(array)):
        line_summa += array[i][len(array[i]) - 1 - i]
    if line_summa != summa:
        return False

    return True


mass = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6],
]

if is_magic(mass):
    print('List is magic')
else:
    print('List is not magic')

