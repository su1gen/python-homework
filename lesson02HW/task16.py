# Мелкая монета для зарплаты. Напишите программу, которая вычисляет сумму денег,
# которую человек заработает в течение периода времени, если в первый день его зарплата
# составит одну копейку, во второй день две копейки и каждый последующий день будет
# удваиваться. Программа должна запросить у пользователя количество дней, вывести
# таблицу, показывающую зарплату за каждый день, и затем показать заработную плату до
# налоговых и прочих удержаний в конце периода.
# Итоговый результат должен быть выведен в рублях, а не в количестве копеек

days = int(input('Введите количество дней '))
start_payment = 0.01
summa = 0

for i in range(1, days + 1):
    day_salary = round(start_payment * i, 2)
    summa += day_salary
    print(f'Зарплата за {i} день: {day_salary} рублей')

print(f'Общая зарплата: {summa} рублей')