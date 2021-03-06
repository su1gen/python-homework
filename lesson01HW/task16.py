# Дни в феврале. Февраль обычно имеет 28 дней. Но в високосный год в феврале 29 дней.
# Напишите программу, которая просит пользователя ввести год. Затем она должна пока-
# зать количество дней в феврале в этом году. Для определения високосных лет исполь-
# зуйте следующие критерии.
# • Определить, делится ли год на 100. Если да, то этот год високосный тогда и только
# тогда, если он также делится на 400. Например, 2000 является високосным годом,
# а 2100 нет.
# • Если год не делится на 100, то этот год високосный тогда и только тогда, если он де-
# лится на 4. Например, 2008 является високосным годом, но 2009 нет.

year = int(input('Введите год:\n'))
days = 28

if year % 100 == 0:
    if year % 400 == 0:
        days = 29
else:
    if year % 4 == 0:
        days = 29

print(f'В {year} году в феврале {days} дней.')
