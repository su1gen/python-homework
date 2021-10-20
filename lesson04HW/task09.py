# Вывод файла на экран. Допустим, что файл numbers.txt содержит ряд целых чисел и
# существует на диске компьютера. Напишите программу, которая выводит на экран все
# числа в файле.


with open('number_list.txt', 'r') as nums_file:
    for line in nums_file:
        print(int(line))