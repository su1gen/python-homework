# На диске существует файл students. txt. Он содержит несколько записей, и каждая запись
# имеет два поля: имя студента и оценку студента за итоговый экзамен.
# Напишите программу, которая удаляет запись с именем студента "Джон Перц".

import os

students_file = open('students.txt', 'r', encoding='utf8')
temp_file = open('temp.txt', 'w', encoding='utf8')

for line in students_file:
    if 'Джон Перц' not in line:
        temp_file.write(line)

students_file.close()
temp_file.close()

# Удалить исходный файл coffee.txt.
os.remove('students.txt')

# Переименовать временный файл.
os.rename('temp.txt', 'students.txt')