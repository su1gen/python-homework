# 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
# а затем наибольшее из данных чисел.
# 4. Даны имена 2х человек (тип string). Если имена равны,
# то вывести сообщение о том, что люди являются тезками.
# 5. Дано число месяца (тип int). Необходимо определить время года
# (зима, весна, лето, осень) и вывести на консоль.

def get_min_value(a, b, c, d, e):
    min_num = a
    if min_num > b:
        min_num = b
    if min_num > c:
        min_num = c
    if min_num > d:
        min_num = d
    if min_num > e:
        min_num = e
    return min_num


def get_max_value(a, b, c, d, e):
    max_num = a
    if max_num < b:
        max_num = b
    if max_num < c:
        max_num = c
    if max_num < d:
        max_num = d
    if max_num < e:
        max_num = e
    return max_num


def task03_print_5_min_max(a, b, c, d, e):
    min_num = get_min_value(a, b, c, d, e)
    max_num = get_max_value(a, b, c, d, e)
    print(f'Минимальное число: {min_num}')
    print(f'Максимальное число: {max_num}')


def task04_compare_2_human(name1, name2):
    if name1 == name2:
        print('Имена равны!')
    else:
        print('Имена не равны!')


def task05_print_season(month_number):
    if month_number == 12 or month_number == 1 or month_number == 2:
        print('Зима')
    elif 2 < month_number < 6:
        print('Весна')
    elif 5 < month_number < 9:
        print('Лето')
    elif 8 < month_number < 12:
        print('Осень')
    else:
        print('Нет такого месяца!')


task03_print_5_min_max(1, 5, 8, 3, 5)
task04_compare_2_human('Юлия', 'Юлия')
task05_print_season(2)
