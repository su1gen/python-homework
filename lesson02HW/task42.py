# Калории за счет жиров и углеводов. Диетолог работает в спортивном клубе и дает
# рекомендации клиентам в отношении диеты. В рамках своих рекомендаций он запрашивает у
# клиентов количество граммов жиров и углеводов, которые они употребили за день.
# Затем на основе приведенной ниже формулы он вычисляет количество калорий, которые
# получаются в результате употребления жиров:
# калории от жиров = граммы жиров х 9.
# Затем на основе еще одной формулы он вычисляет количество калорий, которые получаются в результате
# употребления углеводов:
# калории от углеводов = граммы углеводов х 4.
# Диетолог просит вас написать программу, которая выполнит эти расчеты.

def get_calories_from_fats(fats_amount):
    return fats_amount * 9


def get_calories_from_carbohydrates(carbohydrates_amount):
    return carbohydrates_amount * 4


def main():
    fats = float(input('Введите количество жиров '))
    carbohydrates = float(input('Введите количество углеводов '))

    calories_from_fats = get_calories_from_fats(fats)
    calories_from_carbohydrates = get_calories_from_carbohydrates(carbohydrates)

    print(f'Калорий с жиров: {calories_from_fats}')
    print(f'Калорий с углеводов: {calories_from_carbohydrates}')


if __name__ == '__main__':
    main()

