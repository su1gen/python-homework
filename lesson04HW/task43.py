# Лотерея PowerBall. Для того чтобы сыграть в лотерею PowerBall, покупают билет, в котором имеется пять
# чисел от 1 до 69 и число "PowerBall" в диапазоне от 1 до 26. (Эти
# числа можно выбрать самому либо дать билетному автомату их выбрать за вас случайным образом.)
# Затем в заданный день автомат случайным образом отбирает выигрышный ряд чисел. Если первые пять
# чисел совпадают с первыми пятью выигрышными числами в любом порядке, и ваше число PowerBall соответствует выигрышному числу
# PowerBall, то вы выигрываете джекпот, который составляет очень крупную сумму денег.
# Если ваши числа совпадают лишь с некоторыми выигрышными числами, то вы выигрываете меньшую сумму в
# зависимости от того, сколько выигрышных номеров совпало .
# Среди исходного кода авы 8, а также в подпапке data "Решений задач по программированию"
# соответствующей главы вы найдете файл с именем pbnumbers.txt, содержащий
# выигрышные номера PowerBall, которые были отобраны между 3 февраля 201 О и 11 мая
# 2016 (файл содержит 654 наборов выигрышных чисел). Рис. 8.6 показывает пример первых нескольких
# строк содержимого этого файла. Каждая строка в файле содержит набор
# из шести чисел, которые были выбраны в заданную дату. Числа отделены пробелом,
# и последнее число в каждой строке является числом PowerBall для этого дня. Например,
# первая строка в файле показывает числа за 3 февраля 201 О, которые равнялись 17, 22, 36,
# 37, 52, и число PowerBall, равное 24.

import random


def generate_file():
    with open('pbnumbers.txt', 'w', encoding='utf8') as num_file:
        for i in range(100):
            num_line = []
            for j in range(5):
                num_line.append(random.randint(1, 69))
            num_line.append(random.randint(1, 26))
            num_file.write(' '.join(str(item) for item in num_line) + '\n')


def get_amount(item):
    return item[1]

# employees.sort(key=get_salary, reverse=True)

num_list = []
#
with open('pbnumbers.txt', 'r', encoding='utf8') as num_file:
    for line in num_file:
        num_list += line.split()
#
print(num_list)

checked_list = []
counted_num_list = []
powerballs = num_list[5::6]
print(powerballs)

for num in num_list:
    if num not in checked_list:
        checked_list.append(num)
        counted_num_list.append([num, num_list.count(num)])


counted_num_list.sort(key=get_amount, reverse=True)

max_nums = [num[0] for num in counted_num_list[:10]]
min_nums = [num[0] for num in counted_num_list[-10:]]

counted_powerballs = [f'{num}: {num_list.count(num)}' for num in powerballs]

print(' '.join(max_nums))
print(' '.join(min_nums))
print('\n'.join(counted_powerballs))