# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

num1 = int(input('Введите первое число '))
num2 = int(input('Введите второе число '))
num3 = int(input('Введите третье число '))
num4 = int(input('Введите четвертое число '))

max_num = num1
min_num = num1
max_num_count = 1


if min_num > num2:
    min_num = num2

if min_num > num3:
    min_num = num3

if min_num > num4:
    min_num = num4


if max_num == num2:
    max_num_count += 1
elif max_num < num2:
    max_num = num2
    max_num_count = 1

if max_num == num3:
    max_num_count += 1
elif max_num < num3:
    max_num = num3
    max_num_count = 1

if max_num == num4:
    max_num_count += 1
elif max_num < num4:
    max_num = num4
    max_num_count = 1

print(f'Минимальное число: {min_num}')
print(f'Количество максимальных чисел: {max_num_count}')
