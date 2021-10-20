# Напишите программу, которая открывает файл вывода number_list.txt,
# но не стирает содержимое файла, если он уже существует.

with open('number_list.txt', 'a') as nums_file:
    nums_file.write('1' + '\n')
