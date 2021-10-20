# Самый частотный символ. Напишите программу, которая предоставляет пользователю
# возможность ввести строковое значение и выводит на экран символ, который появляется
# в нем наиболее часто.

string = input("Enter text ").replace(' ', '')

checked_list = []
max_count = 0
max_character = ''

for ch in string:
    if ch not in checked_list:
        checked_list.append(ch)
        current_count = string.count(ch)
        if max_count < current_count:
            max_count = current_count
            max_character = ch

print(max_character)

