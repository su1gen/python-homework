# Римские цифры. Напишите программу, которая предлагает пользователю ввести число
# в диапазоне от 1 до 10. Программа должна показать для этого числа римскую цифру.
# Если число находится вне диапазона 1-1О, то программа должна вывести сообщение об
# ошибке.

age = int(input('Ведите число от 1 до 10\n'))

if age == 1:
    print('I')
elif age == 2:
    print('II')
elif age == 3:
    print('III')
elif age == 4:
    print('IV')
elif age == 5:
    print('V')
elif age == 6:
    print('VI')
elif age == 7:
    print('VII')
elif age == 8:
    print('VIII')
elif age == 9:
    print('IX')
elif age == 10:
    print('X')
else:
    print('Вы ввели неверное число')

