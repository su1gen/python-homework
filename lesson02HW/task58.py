# Игра "Камень, ножницы, бумага". Напишите программу, которая дает пользователю
# возможность поиграть с компьютером в игру "Камень, ножницы, бумага". Программа
# должна работать следующим образом:
# 1. Когда программа запускается, генерируется случайное число в диапазоне от 1 до 3.
# Если число равняется 1, то компьютер выбрал камень. Если число равняется 2, то
# компьютер выбрал ножницы. Если число равняется 3, то компьютер выбрал бумагу.
# (Пока не показывайте выбор компьютера.)
# 2. Пользователь вводит на клавиатуре выбранный вариант "камень", "ножницы" или
# "бумага".
# 3. Выбор компьютера выводится на экран.
# 4. Победитель выбирается согласно следующим правилам:
# 0 если один игрок выбирает камень, а другой игрок выбирает ножницы, то побеждает камень (камень разбивает ножницы);
# 0 если один игрок выбирает ножницы, а другой игрок выбирает бумагу, то побеждают ножницы (ножницы режут бумагу);
# 0 если один игрок выбирает бумагу, а другой игрок выбирает камень, то побеждает
# бумага (бумага заворачивает камень);
# 0 если оба игрока делают одинаковый выбор, то для определения победителя нужно
# сыграть повторный раунд.

import random


def get_comp_answer():
    answer_code = random.randint(1, 3)
    if answer_code == 1:
        return 'камень'
    elif answer_code == 2:
        return 'ножницы'
    else:
        return 'бумага'


def get_result(comp_answer, user_answer):
    if comp_answer == user_answer:
        return 'ничья'
    elif comp_answer == 'камень':
        if user_answer == 'ножницы':
            return 'компьютер победил'
        else:
            return 'вы победили'
    elif comp_answer == 'ножницы':
        if user_answer == 'бумага':
            return 'компьютер победил'
        else:
            return 'вы победили'
    else:
        if user_answer == 'камень':
            return 'компьютер победил'
        else:
            return 'вы победили'


comp_answer = get_comp_answer()
user_answer = input('Введите число "камень", "ножницы" или "бумага" ')
result = get_result(comp_answer, user_answer)

print(f'компьютер выбрал {comp_answer}')
print(result)