# Сумма чисел. Допустим, что файл с рядом целых чисел называется numbers.txt и существует на диске компьютера.
# Напишите программу, которая читает все хранящиеся в файле числа и вычисляет их сумму.

summa = 0

with open('number_list.txt', 'r') as nums_file:
    for line in nums_file:
        summa += int(line)

print(summa)