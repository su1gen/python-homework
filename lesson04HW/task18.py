# Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные.
# Президент клуба попросил вас написать две программы:
# • программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиатуры,
# и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь
# поле для имени игрока и поле для счета игрока);
# • программу, которая читает записи из файла golf.txt и выводит их на экран.


def add_fields():
    with open('golf.txt', 'a', encoding='utf8') as golf_file:
        amount = int(input('How many field do you wish to add '))
        for i in range(amount):
            name = input('Enter name ')
            points = int(input('Enter points '))
            golf_file.write(f'{name} {points}\n')


def show_fields():
    with open('golf.txt', 'r', encoding='utf8') as golf_file:
        for line in golf_file:
            print(line.rstrip())

add_fields()
show_fields()