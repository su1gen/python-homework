# Игра в угадывание случайного числа. Напишите программу, которая генерирует случайное число в диапазоне от 1 до 100
# и просит пользователя угадать это число. Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение
# "Слишком много, попробуйте еще раз". Если догадка меньше случайного числа, то программа должна вывести сообщение
# "Слишком мало, попробуйте еще раз". Если пользователь число угадывает,
# то приложение должно поздравить пользователя и сгенерировать новое случайное число, чтобы возобновить игру.
# Необязательное улучшение: улучшите игру, чтобы она вела подсчет догадок, которые
# делает пользователь. Когда пользователь угадывает случайное число правильно,
# программа должна показать количество догадок.


import random

num = random.randint(1, 100)
tries = 0

while True:
    answer = int(input('Введите число '))
    tries += 1
    if answer < num:
        print('Слишком мало, попробуйте еще раз')
    elif answer > num:
        print('Слишком много, попробуйте еще раз')
    else:
        print(f'Вы угадали с {tries} попытки')
        break
