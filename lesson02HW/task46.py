# Футы в дюймы. Один фут равняется 12 дюймам. Напишите функцию feet to inches,
# которая в качестве аргумента принимает количество футов и возвращает количество
# дюймов в этом количестве футов. Примените эту функцию в программе, которая предлагает
# пользователю ввести количество футов и затем показывает количество дюймов
# в этом количестве футов.

def feet_to_inches(feet):
    return feet * 12


def main():
    feet_value = int(input('Введите количество футов '))

    inches = feet_to_inches(feet_value)

    print(f'В {feet_value} футах - {inches} дюймов')


if __name__ == '__main__':
    main()
