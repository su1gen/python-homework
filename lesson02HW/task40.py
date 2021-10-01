# Расходы на автомобиль. Напишите программу, которая просит пользователя ввести
# месячные расходы на следующие нужды, связанные с его автомобилем: платеж по кредиту, страховка, бензин,
# машинное масло, шины и техобслуживание. Затем программа
# должна показать общую месячную стоимость и общую годовую стоимость этих расходов.

def get_monthly_cost(credit_value, insurance_value, benzine_value, oil_value, tire_value, maintenance_value):
    return credit_value + insurance_value + benzine_value + oil_value + tire_value + maintenance_value


def get_yearly_cost(monthly_cost_value):
    return monthly_cost_value * 12


def main():
    credit = float(input('Введите платеж по кредиту '))
    insurance = float(input('Введите затраты на страховку '))
    benzine = float(input('Введите затраты на бензин '))
    oil = float(input('Введите затраты на машинное масло '))
    tire = float(input('Введите затраты на шины '))
    maintenance = float(input('Введите затраты на техобслуживание '))

    monthly_cost = get_monthly_cost(credit, insurance, benzine, oil, tire, maintenance)
    yearly_cost = get_yearly_cost(monthly_cost)

    print(f'Месячные затраты: {monthly_cost}')
    print(f'Затраты за год: {yearly_cost}')


if __name__ == '__main__':
    main()