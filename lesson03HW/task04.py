# Напишите функцию, которая принимает список в качестве аргумента (допустим, что список содержит целые числа)
# и возвращает сумму значений в списке.

def get_sum(mass):
    return sum(mass)


nums = list(range(10))

print(get_sum(nums))