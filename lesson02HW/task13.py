# Пройденное расстояние. Пройденное транспортным средством расстояние можно вычислить следующим образом:
# расстояние = скорость х время.
# Например, если поезд движется со скоростью 90 км/ч в течение трех часов, то пройденное расстояние составит 270 км.
# Напишите программу, которая запрашивает у пользователя скорость транспортного средства (в км/ч) и количество часов,
# которое оно двигалось. Затем она должна применить цикл для вывода расстояния, пройденного транспортным средством
# для каждого часа этого периода времени. Вот пример требуемого
# результата:
# Какая скорость транспортного средства в км/ч? 40 IEnterl
# Сколько часов оно двигалось? 3 IEnterl
# Час Пройденное расстояние
# 1 40
# 2 80
# 3 120


speed = int(input('Введите скорость '))
time = int(input('Введите время '))

for i in range(1, time + 1):
    distance = speed * i
    print(f'За {i} час пройдено {distance}')
