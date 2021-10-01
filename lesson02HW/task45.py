# Месячный налог с продаж. Розничная компания должна зарегистрировать отчет о месячном
# налоге с продаж с указанием общего налога с продаж за месяц и взимаемых сумм
# муниципального и федерального налогов с продаж. Федеральный налог с продаж составляет 5%,
# муниципальный налог с продаж - 2,5%. Напишите программу, которая просит
# пользователя ввести общий объем продаж за месяц. Из этого значения приложение должно рассчитать и показать:
# • сумму муниципального налога с продаж;
# • сумму федерального налога с продаж;
# • общий налог с продаж (муниципальный плюс федеральный).

FED_TAX_RATE = 0.05
MUN_TAX_RATE = 0.025


def get_purchase_amount():
    return float(input('Введите общий объем продаж за месяц '))


def count_tax(purchase_amount, tax_rate):
    return round(purchase_amount * tax_rate, 2)


def main():
    current_amount = get_purchase_amount()

    mun_tax = count_tax(current_amount, FED_TAX_RATE)
    fed_tax = count_tax(current_amount, MUN_TAX_RATE)

    all_tax = fed_tax + mun_tax

    print(f'Сумма муниципального налога: {mun_tax}')
    print(f'Сумма федерального налога: {fed_tax}')
    print(f'Общий налог: {all_tax}')


if __name__ == '__main__':
    main()