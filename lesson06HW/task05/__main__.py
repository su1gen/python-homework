# Класс Car. Напишите класс под названием Car (Легковой автомобиль), который имеет
# приведенные ниже атрибуты данных:
# • _year _ model (для модели указанного года выпуска);
# • rttake (для фирмы-изготовителя автомобиля);
# • _ speed (для текущей скорости автомобиля).
# Класс car должен иметь метод _ ini t _ (), который в качестве аргументов принимает
# модель указанного года выпуска и фирму-изготовителя. Эти значения должны быть присвоены атрибутам данных _year_model и _
# make объекта. Он также должен присвоить О
# атрибуту данных _ speed.
# Этот класс также должен иметь методы:
# • метод accelerate () (ускоряться) при каждом его вызове должен прибавлять 5 в атрибут данных _ speed;
# • метод break () (тормозить) при каждом его вызове должен вычитать 5 из атрибута
# данных speed;
# • метод get speed () (получить скорость) должен возвращать текущую скорость.
# Далее разработайте программу, которая создает объект car и пятикратно вызывает метод
# accelerate ().После каждого вызова метода accelerate () она должна получать текущую
# скорость автомобиля и выводить ее на экран. Затем она должна пятикратно вызвать
# метод break () . После каждого вызова метода break () она должна получать текущую
# скорость автомобиля и выводить ее на экран.

from lesson06HW.task05.car import Car

if __name__ == '__main__':
    car = Car(2000, 2002)

    car.accelerate_speed()
    print(car.get_speed())
    car.accelerate_speed()
    print(car.get_speed())
    car.accelerate_speed()
    print(car.get_speed())
    car.accelerate_speed()
    print(car.get_speed())
    car.accelerate_speed()
    print(car.get_speed())
    car.break_speed()
    print(car.get_speed())
    car.break_speed()
    print(car.get_speed())
    car.break_speed()
    print(car.get_speed())
    car.break_speed()
    print(car.get_speed())
    car.break_speed()
    print(car.get_speed())