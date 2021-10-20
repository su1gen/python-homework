# Измените программу, которую вы написали в задаче 4 таким образом, чтобы она суммировала
# все прочитанные из файла числа и выводила на экран их сумму

with open('number_list.txt', 'r') as nums_file:
    for line in nums_file:
         summa += int(line)

ternp_file = open ( 'ternp. txt', 'w')

print(summa)