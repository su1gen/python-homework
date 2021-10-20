# Напишите программу, которая делает следующее: открывает выходной файл с именем
# number_list.txt, применяет цикл для записи в файл чисел с 1 по 100, а затем закрывает
# файл.



with open('number_list.txt', 'w') as nums_file:
    for i in range(1, 101):
        nums_file.write(str(i) + '\n')