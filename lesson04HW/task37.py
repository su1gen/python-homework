# Анализ символов. Среди исходного кода главы 8, а также в подпапке data "Решений задач по программированию"
# соответствующей главы вы найдете файл text.txt. Напишите
# программу, которая читает содержимое файла и определяет:
# • количество букв в файле в верхнем регистре;
# • количество букв в файле в нижнем регистре;
# • количество цифр в файле;
# • количество пробельных символов в файле.

upper = 0
lower = 0
digit = 0
space = 0

with open('text.txt', 'r', encoding='utf8') as text_file:
    text = text_file.read()
    for ch in text:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
        if ch.isdigit():
            digit += 1
        if ch.isspace():
            space += 1


print(upper, lower, digit, space)

