# Поиск имени. Среди исходного кода главы 7, а также в подпапке data "Решений задач
# по программированию" соответствующей главы вы найдете приведенные ниже файлы:
# • GirlsNames.txt - файл содержит список 200 самых популярных имен, данных девочкам,
# родившимся в США между 2000 и 2009 годами;
# • BoyNames.txt- файл содержит список 200 самых популярных имен, данных мальчикам,
# родившимся в США между 2000 и 2009 годами.
# Напишите программу, которая считывает содержимое этих двух файлов в два отдельных
# списка. Пользователь должен иметь возможность ввести имя мальчика, имя девочки или
# оба имени, и приложение должно вывести сообщения о том, что введенные имена находятся среди самых популярных имен.


girls_names = []
boys_names = []

girls_names_file = open('GirlsNames.txt', 'r')

for name in girls_names_file:
    girls_names.append(name.rstrip('\n'))

girls_names_file.close()

boys_names_file = open('BoysNames.txt', 'r')

for name in boys_names_file:
    boys_names.append(name.rstrip('\n'))

boys_names_file.close()


girl_name = input('Enter girl name ')
boy_name = input('Enter boy name ')

if girl_name in girls_names:
    print('Girl name is in the file')
else:
    print('Girl name is not in the file')

if boy_name in boys_names:
    print('Boy name is in the file')
else:
    print('Boy name is not in the file')

