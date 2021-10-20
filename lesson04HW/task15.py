# Программа записи файла со случайными числами. Напишите программу, которая
# пишет в файл ряд случайных чисел. Каждое случайное число должно быть в диапазоне
# от 1 до 500. Приложение должно предоставлять пользователю возможность назначать
# количество случайных чисел, которые будут содержаться в файле.

import random

amount = int(input('Enter amount of numbers '))

with open('random_numbers.txt', 'w', encoding='utf8') as num_file:
    for i in range(amount):
        random_num = random.randint(1, 500)
        num_file.write(str(random_num) + '\n')
