# 1. считать с консоли 6 числовых значений и записать в файл.
# 2. прочитать из файла значения и записать в список, посчитать сумму и среднее
# 3. 1 и 2 сделать для матрицы(2х3)

# ------------------1------------------
numbers = []

for i in range(6):
    num = int(input('Enter a number '))
    numbers.append(num)


num_file = open('numbers.txt', 'w')

for i in numbers:
    num_file.write(str(i) + '\n')

num_file.close()



# ----------------2--------------
nums_list = []

num_file = open('numbers.txt', 'r')

for line in num_file:
    nums_list.append(int(line))

num_file.close()

nums_sum = sum(nums_list)
nums_avg = round(nums_sum / len(nums_list), 2)

print(nums_list, nums_sum, nums_avg)



# --------------------3----------------

nums_list = []

num_file = open('numbers.txt', 'r')

mass = []
i = 0
for line in num_file:
    mass.append(int(line))
    i += 1
    if i % 3 == 0:
        nums_list.append(mass)
        mass = []

num_file.close()

summa = 0
count = 0

for item in nums_list:
    for j in item:
        summa += j
        count += 1


avg = summa / count

print(nums_list, summa, avg)