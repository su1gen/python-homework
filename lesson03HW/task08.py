# Генератор лотерейных чисел. Разработайте программу, которая генерирует семизначную комбинацию лотерейных чисел.
# Программа должна сгенерировать семь случайных чисел, каждое в диапазоне от О до 9,
# и присвоить каждое число элементу списка. (Случайные числа рассматривались в главе 5.)
# Затем напишите еще один цикл, который показывает содержимое списка.

import random

mass = []

for i in range(7):
    num = random.randint(0, 9)
    mass.append(num)

for i in mass:
    print(i, end=' ')
