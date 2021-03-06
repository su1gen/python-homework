# Средняя толщина дождевых осадков. Напишите программу, которая применяет вложенные циклы для сбора данных и
# вычисления средней толщины дождевых осадков за ряд лет. Программа должна сначала запросить количество лет. Внешний
# цикл будет выполнять одну итерацию для каждого года. Внутренний цикл будет делать двенадцать итераций,
# одну для каждого месяца. Каждая итерация внутреннего цикла запрашивает у пользователя миллиметры дождевых осадков в
# течение этого месяца. После всех итераций программа должна вывести количество месяцев, общее количество
# миллиметров дождевых осадков и среднюю толщину дождевых осадков в месяц в течение всего периода

years = int(input('Введите количество лет '))
summa = 0

for i in range(years):
    for month in range(12):
        precipitation = float(input(f'Введите осадки за {month + 1} месяц {i + 1} года '))
        summa += precipitation

months = years * 12
average_precipitations = round(summa / months, 2)

print(f'Количество месяцев: {months}')
print(f'Общее количество миллиметров дождевых осадков: {summa}')
print(f'Средняя толщина дождевых осадков в месяц: {average_precipitations}')
