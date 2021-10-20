# Напишите программу, которая открывает файл my_name.txt, созданный программой в задаче 1,
# читает ваше имя из файла, выводит имя на экран и затем закрывает файл.

with open('my_name.txt', 'r') as name_file:
    for line in name_file:
        print(line)