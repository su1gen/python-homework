# 6.Дан массив размерности N, найти наименьший элемент массива
# и вывести на консоль (если наименьших элементов несколько —
# вывести их индексы).
# 7.Поменять наибольший и наименьший элементы массива местами.
# Пример: дан массив {4, -5, 0, 6, 8}.
# После замены будет выглядеть {4, 8, 0, 6, -5}.

arr = [1, 2, 3, 1, 5]

min_value = min(arr)
max_value = max(arr)

print(min_value)

if arr.count(min_value) > 1:
    for i in range(len(arr) - 1):
        if arr[i] == min_value:
            print(i, end=' ')
