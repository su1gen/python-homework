# Классификатор возраста. Напишите программу, которая просит пользователя ввести
# возраст человека. Программа должна определить, к какой категории этот человек при-
# надлежит: младенец, ребенок, подросток или взрослый, и вывести соответствующее со-
# общение. Ниже приведены возрастные рекомендации:
# • если возраст 1 год или меньше, то он или она - младенец;
# • если возраст старше l года, но моложе 13 лет, то он или она- ребенок;
# • если возраст не менее 13 лет, но моложе 20 лет, то он или она - подросток;
# • если возраст более 20 лет, то он или она- взрослый.

age = int(input('Введите возраст\n'))

if age <= 1:
    print('младенец')
elif age <= 13:
    print('ребенок')
elif age <= 20:
    print('подросток')
else:
    print('взрослый')
