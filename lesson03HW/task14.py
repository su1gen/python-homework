# Данные о населении. Среди исходного кода главы 7, а также в подпапке data "Решений
# задач по программированию" соответствующей главы вы найдете файл USPopulation.txt.
# Этот файл содержит данные о среднегодовой численности населения США в тысячах с
# 1950 по 1990 годы. Первая строка в файле содержит численность населения в 1950 году,
# вторая строка - численность населения в 1951 году и т. д.
# Напишите программу, которая считывает содержимое файла в список. Программа должна показать приведенные ниже данные:
# • среднегодовое изменение численности населения в течение указанного периода времени;
# • год с наибольшим увеличением численности населения в течение указанного периода
# времени;
# • год с наименьшим увеличением численности населения в течение указанного периода
# времени.


population_list = []
population_diff_sum = 0


population_file = open('population.txt', 'r')

for item in population_file:
    population_list.append(float(item.rstrip('\n')))

population_file.close()

max_diff = 0
min_diff = 0

for i in range(len(population_list) - 1):

    population_diff = population_list[i] - population_list[i + 1]
    population_diff_sum += population_diff

    if i == 0:
        max_diff = population_diff
        min_diff = population_diff

    if population_diff > max_diff:
        max_diff = population_diff
    if population_diff < min_diff:
        min_diff = population_diff

average_diff = population_diff_sum / (len(population_list) - 1)



print(f'Avarage: {average_diff}')
print(f'Min: {min_diff}')
print(f'Max: {max_diff}')