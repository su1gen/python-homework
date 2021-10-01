# Счетчик четных/нечетных чисел. В этой главе вы увидели пример написания алгоритма,
# который определяет четность или нечетность числа. Напишите программу,
# которая генерирует 100 случайных чисел и подсчитывает количество четных и нечетных
# случайных чисел.

import random

even = 0
odd = 0


for i in range(100):
    num = random.randint(0, 1000)
    if num % 2 == 0:
        even += 1
    else:
        odd += 1


print(f'Четных чисел {even}')
print(f'Нечетных чисел {odd}')
