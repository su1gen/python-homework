# Список простых чисел. Это упражнение предполагает, что вы уже написали функцию
# is _pr ime в задаче 17. Напишите еще одну программу, которая показывает все простые
# числа от 1 до 100. Программа должна иметь цикл, который вызывает функцию is prime.

def is_prime(num):
    for i in range(1, num + 1):
        if num % i == 0:
            if i != 1 and i != num:
                return False
    return True


for i in range(1, 101):
    if is_prime(i):
        print(i)