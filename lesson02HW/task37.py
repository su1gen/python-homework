# Конвертер километров. Напишите программу, которая просит пользователя ввести расстояние
# в километрах и затем это расстояние преобразует в мили. Формула преобразования:
# мили = километры х 0.6214.

def get_kilometres():
    return float(input('Введите растояние в километрах '))


def convert_to_miles(kilometres):
    return kilometres * 0.6214


kilometres = get_kilometres()

miles = convert_to_miles(kilometres)

print(miles)
