# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

from task_lib import *

num1 = int(input('Введите первое число '))
num2 = int(input('Введите второе число '))
num3 = int(input('Введите третье число '))
num4 = int(input('Введите четвертое число '))


min_num = get_min_value(num1, num2, num3, num4)
max_num = get_max_value(num1, num2, num3, num4)

count_max = get_count_max_values(num1, num2, num3, num4)

# if max_num == num2:
#     max_num_count += 1
# elif max_num < num2:
#     max_num = num2
#     max_num_count = 1
#
# if max_num == num3:
#     max_num_count += 1
# elif max_num < num3:
#     max_num = num3
#     max_num_count = 1
#
# if max_num == num4:
#     max_num_count += 1
# elif max_num < num4:
#     max_num = num4
#     max_num_count = 1

print(f'Минимальное число: {min_num}')
print(f'Количество максимальных чисел: {count_max}')
