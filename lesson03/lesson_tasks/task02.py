# 2.ввести 10 целых значений с консоли и разместить в
# 2 масива четные и нечетные
# 3.подсчитать сколько четные и нечетные
# 4.сумма елементов в каждом масиве и среднее арифметическое
# 5.поменять четные позиции в первом масиве на значения
# нечетных позиций из 2 массива

def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


arr_even = []
arr_odd = []

for i in range(1, 11):
    num = int(input(f'Введите {i} число '))
    if is_even(num):
        arr_even.append(num)
    else:
        arr_odd.append(num)


arr_even_len = len(arr_even)
arr_odd_len = len(arr_odd)

arr_even_sum = 0
arr_odd_sum = 0

for item in arr_even:
    arr_even_sum += item

for item in arr_odd:
    arr_odd_sum += item

arr_even_average = round(arr_even_sum / arr_even_len, 2)
arr_odd_average = round(arr_odd_sum / arr_odd_len, 2)

print(f'Четный массив {arr_even}, его длинна: {arr_even_len}, сумма элементов: {arr_even_sum}, среднее значение : {arr_even_average}')
print(f'Нечетный массив {arr_odd}, его длинна: {arr_odd_len}, сумма элементов: {arr_odd_sum}, среднее значение : {arr_odd_average}')

for i in range(arr_even_len):
    if not is_even(i):
        arr_even[i] = arr_odd[i - 1]

print(f'Четный массив после преображения {arr_even}')
