# Напишите цикл, который вычисляет сумму приведенного ниже числового ряда:
# 1/30 + 2/29 + 3/28 ... + 30/1

num = 30
summa = 0

for i in range(1, 31):
    summa += i / num
    num -= 1

    print(round(summa, 2))