# Игра в подсчитывание монет. Создайте игру, которая просит пользователя ввести не-
# обходимое количество монет, чтобы получился ровно один рубль. Программа должна
# предложить пользователю ввести количество монет достоинством 5, 1О и 50 копеек.
# Если итоговое значение введенных монет равно одному рублю, то программа должна
# поздравить пользователя с выигрышем. В противном случае программа должна вывести
# сообщение, говорящее о том, была ли введенная сумма больше или меньше одного
# рубля. Подумайте о варианте игры, где вместо рубля используется доллар и разменные
# монеты: пенс, пятицентовик, десятицентовик и четвертак.

coin_5 = int(input('Введите количество монет номиналом 5 копеек\n'))
coin_10 = int(input('Введите количество монет номиналом 10 копеек\n'))
coin_50 = int(input('Введите количество монет номиналом 50 копеек\n'))

coins_sum = coin_5 * 5 + coin_10 * 10 + coin_50 * 50

if coins_sum > 100:
    print('Сумма больше одного рубля!')
elif coins_sum < 100:
    print('Сумма меньше одного рубля!')
else:
    print('Сумма равна одному рублю!')
