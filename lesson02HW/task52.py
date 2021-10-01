# Средний балл и его уровень. Напишите программу, которая просит пользователя ввести пять экзаменационных оценок.
# Программа должна показать буквенный уровень
# оценки для каждой оценки и средний балл. Напишите в программе приведенные ниже
# функции:
# • calc average - функция должна принимать в качестве аргументов пять оценок и
# возвращать средний балл;
# • determine grade - функция должна принимать в качестве аргумента оценку и возвращать буквенный уровень оценки,
# опираясь на приведенную в табл. 5.3 классификации.
# Таблица 5.3. Шкала классификации
# Оценка Уровень
# 90 и выше А
# 80-89 в
# 70-79 с
# 60-69 D
# Ниже 60 F


def calc_average(rate1, rate2, rate3, rate4, rate5):
    return (rate1 + rate2 + rate3 + rate4 + rate5) / 5


def determine_grade(average_rate):
    if average_rate < 60:
        return 'F'
    elif average_rate < 70:
        return 'D'
    elif average_rate < 80:
        return 'C'
    elif average_rate < 90:
        return 'B'
    else:
        return 'A'


num1 = int(input('Введите первую оценку '))
num2 = int(input('Введите вторую оценку '))
num3 = int(input('Введите третью оценку '))
num4 = int(input('Введите четвертую оценку '))
num5 = int(input('Введите пятую оценку '))


average = calc_average(num1, num2, num3, num4, num5)

grade = determine_grade(average)

print(f'Уровень оценки: {grade}')
