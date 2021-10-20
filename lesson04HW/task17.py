# Обработка исключений. Измените программу, которую вы написали для задания 6
# таким образом, чтобы она обрабатывала приведенные ниже исключения:
# • она должна обрабатывать любые исключения IOError, которые вызываются, когда
# файл открыт, и данные из него считываются;
# • она должна обрабатывать любые исключения ValueError, которые вызываются, когда
# прочитанные из файла значения конвертируются в числовой тип.


summa = 0
count = 0

try:
    with open('number_list.txt', 'r') as nums_file:
        for line in nums_file:
            try:
                summa += int(line)
            except ValueError:
                print('Value error')
            count += 1
except IOError:
    print('IOError')

avg = round(summa / count, 2)

print(avg)