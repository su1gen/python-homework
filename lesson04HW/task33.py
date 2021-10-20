# Принтер дат. Напишите программу, которая считывает от пользователя строковое значение,
# содержащее дату в формате дд/мм/гггг. Она должна напечатать дату в формате
# 12 марта 2018 г.

date = input('Enter date ')

date_list = date.split('/')

new_date = date_list[0] + ' '

if date_list[1] == '01':
    new_date += 'января '
elif date_list[1] == '02':
    new_date += 'февраля '
elif date_list[1] == '03':
    new_date += 'марта '
elif date_list[1] == '04':
    new_date += 'апреля '
elif date_list[1] == '05':
    new_date += 'мая '
elif date_list[1] == '06':
    new_date += 'июня '
elif date_list[1] == '07':
    new_date += 'июля '
elif date_list[1] == '08':
    new_date += 'августа '
elif date_list[1] == '09':
    new_date += 'сентября '
elif date_list[1] == '10':
    new_date += 'октября '
elif date_list[1] == '11':
    new_date += 'ноября '
elif date_list[1] == '12':
    new_date += 'декабря '

new_date += date_list[2] + ' г.'

print(new_date)