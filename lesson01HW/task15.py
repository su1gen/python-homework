# Калькулятор времени. Напишите программу, которая просит пользователя ввести
# количество секунд и работает следующим образом.
# • В минуте 60 секунд. Если число введенных пользователем секунд больше или равно
# 60, то программа должна преобразовать число секунд в минуты и секунды.
# • В часе 3 600 секунд. Если число введенных пользователем секунд больше или равно
# 3 600, то программа должна преобразовать число секунд в часы, минуты и секунды.
# • В дне 86 400 секунд. Если число введенных пользователем секунд больше или равно
# 86 400, то программа должна преобразовать число секунд в дни, часы, минуты и
# секунды.

input_seconds = int(input('Введите количество секунд\n'))

if input_seconds < 60:
    print(f'{input_seconds} секунд')
elif input_seconds < 3600:
    minutes = input_seconds // 60
    seconds = input_seconds % 60
    print(f'{minutes} минут и {seconds} секунд')
elif input_seconds < 86400:
    hours = input_seconds // 3600
    minutes = input_seconds % 3600 // 60
    seconds = input_seconds % 60
    print(f'{hours} часов, {minutes} минут и {seconds} секунд')
else:
    days = input_seconds // 86400
    hours = input_seconds % 86400 // 3600
    minutes = input_seconds % 3600 // 60
    seconds = input_seconds % 60
    print(f'{days} дней, {hours} часов, {minutes} минут и {seconds} секунд')