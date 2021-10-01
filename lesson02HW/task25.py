# Используя циклы и метод:
# print("*"), print(" ", end =""), print("\n") (для перехода на новую строку).
# Выведите на экран:
# · прямоугольник
# · прямоугольный треугольник
# · равносторонний треугольник
# · ромб

print('Прямоугольник\n')

for i in range(1, 5):
    for j in range(1, 14):
        print('*', end='')
    print()

print('\nПрямоугольный треугольник\n')

for i in range(1, 8):
    for j in range(1, i + 1):
        print('*', end='')
    print()

print('\nРавносторонний треугольник\n')

stars = 1
line_length = 15

for i in range(0, 8):

    stars_in_line = stars + i * 2
    spaces_in_line = line_length - stars_in_line

    for space in range(int(spaces_in_line / 2)):
        print(" ", end="")

    for j in range(stars_in_line):
        print('*', end='')

    for space in range(int(spaces_in_line / 2)):
        print(" ", end="")

    print()

print('\nРомб\n')

line_length = 15
stars_in_line = 1

for i in range(line_length):
    if i < (line_length // 2 + 1):
        stars_in_line = i * 2 + 1
        spaces_in_line = line_length - stars_in_line
    else:
        stars_in_line -= 2
        spaces_in_line = line_length - stars_in_line

    for space in range(int(spaces_in_line / 2)):
        print(" ", end="")

    for j in range(stars_in_line):
        print('*', end='')

    for space in range(int(spaces_in_line / 2)):
        print(" ", end="")

    print()
