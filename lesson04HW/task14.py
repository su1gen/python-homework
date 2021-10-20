# Среднее арифметическое чисел. Допустим, что файл с рядом целых чис~л называется
# numbers.txt и существует на диске компьютера. Напишите программу, которая вычисляет
# среднее арифметическое всех хранящихся в файле чисел.



summa = 0
count = 0

with open('number_list.txt', 'r') as nums_file:
    for line in nums_file:
        summa += int(line)
        count += 1

avg = round(summa / count, 2)

print(avg)