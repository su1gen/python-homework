# Оценщик малярных работ. Малярная компания установила, что на каждые 10 квадратных
# метров поверхности стены требуется 5 литров краски и 8 часов работы. Компания
# взимает за работу 2000 руб. в час. Напишите программу, которая просит пользователя
# ввести площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски.
# Программа должна показать следующие данные:
# • количество требующихся емкостей краски;
# • количество требующихся рабочих часов;
# • стоимость краски;
# • стоимость работы;
# • общая стоимость малярных работ.

def get_dyes_amount(area):
    return area / 5


def get_dyes_value(dyes_amount, dye_value):
    return dyes_amount * dye_value


def get_spent_hours(area):
    return area / 8


def get_work_value(hours, value):
    return hours * value


def main():
    wall_area = int(input('Введите площадь поверхности окрашиваемой стены '))
    dye_value = int(input('Введите цену 5-литровой емкости краски '))

    dyes_amount = get_dyes_amount(wall_area)
    work_hours = get_spent_hours(wall_area)

    dyes_value = get_dyes_value(dyes_amount, dye_value)
    work_value = get_work_value(work_hours, 2000)

    all_value = dyes_value + work_value

    print(f'количество требующихся емкостей краски: {dyes_amount}')
    print(f'количество требующихся рабочих часов: {work_hours}')
    print(f'стоимость краски: {dyes_value}')
    print(f'стоимость работы: {work_value}')
    print(f'общая стоимость малярных работ: {all_value}')


if __name__ == '__main__':
    main()
