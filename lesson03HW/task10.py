# Проrрамма анализа чисел. Разработайте программу, которая просит пользователя ввести ряд из 20 чисел.
# Программа должна сохранить числа в списке и затем показать приведенные ниже данные:
# • наименьшее число в списке;
# • наибольшее число в списке;
# • сумму чисел в списке;
# • среднее арифметическое значение чисел в списке.


mass = []

for i in range(20):
    num = int(input('Input value '))
    mass.append(num)

summa = sum(mass)
average = round(summa / len(mass), 2)
min = min(mass)
max = max(mass)


print(f'Sum: {summa}')
print(f'Average: {average}')
print(f'Min: {min}')
print(f'Max: {max}')