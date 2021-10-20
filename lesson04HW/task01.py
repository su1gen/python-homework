# Напишите программу, которая открывает файл вывода my_name.txt, пишет в него ваше
# имя и затем его закрывает.

with open('my_name.txt', 'w') as name_file:
    name_file.write('My name')