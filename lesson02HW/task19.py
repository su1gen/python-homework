# Рост платы за обучение. В заданном университете обучение студента-очника составляет 45 ООО рублей в семестр.
# Было объявлено, что плата за обучение будет повышаться на
# 3% каждый год в течение следующих 5 лет. Напишите программу с циклом, который
# выводит плановую сумму за обучение в семестр в течение следующих 5 лет.

rate = 45000
coefficient = 0.03

for i in range(1, 6):
    rate += round(rate * coefficient, 2)
    print(f'Плата за {i} год: {rate} рублей')