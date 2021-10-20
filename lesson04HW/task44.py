# Цены на бензин. Среди исходного кода главы 8, а также в подпапке data "Решений задач по программированию"
# соответствующей главы, вы найдете файл GasPrices.txt. Этот
# файл содержит еженедельные средние цены за галлон бензина в США, начиная 5 апреля
# 1993 года и заканчивая 26 августа 2013 года. На рис. 8.7 показан пример первых нескольких строк данного файла.
# Каждая строка в файле содержит среднюю цену за галлон бензина в указанный день
# и отформатирована следующим образом:
# ММ-дц-ГГГГ:Цена
# где мм - двухзначный месяц; дц - двухзначный день; гггг - четырехзначный год;
# Цена - это средняя цена галлона бензина в указанный день.
# В рамках этого задания необходимо написать одну или несколько программ, которые
# считывают содержимое данного файла и выполняют приведенные ниже вычисления.
# • Средняя цена за год: вычисляет среднюю цену бензина за год для каждого года
# в файле. (Данные файла начинаются апрелем 1993 и заканчиваются августом 2013.
# Используйте данные, предоставленные за период с 1993 по 2013 годы.)
# • Средняя цена за месяц: вычисляет среднюю цену в каждом месяце в файле.
# • Наибольшая и наименьшая цены в году: в течение каждого года в файле определяет дату
# и величину самой низкой и самой высокой цены.
# • Список цен, упорядоченный по возрастанию: генерирует текстовый файл, в котором даты
# и цены отсортирован~~ в возрастающем порядке.
# • Список цен, упорядоченный по увеличению: генерирует текстовый файл, в котором даты
# и цены отсортированы в убывающем порядке.
# Для выполнения всех этих вычислений можно написать одну программу или несколько
# разных программ, одну для каждого вычисления.


def get_list():

    changed_list = []

    with open('gasprices.txt', 'r', encoding='utf8') as num_file:
        for item in num_file:
            list = item.strip().split(':')
            new_list = list[0].split('-') + [list[1]]
            changed_list.append(new_list)

    return changed_list



def print_year_avg_price(changed_list):
    current_year = changed_list[0][2]
    year_price_sum = 0
    year_price_count = 0

    for i in range(len(changed_list)):

        if current_year == changed_list[i][2]:

            year_price_sum += float(changed_list[i][3])
            year_price_count += 1

        else:
            avg_price = round(year_price_sum / year_price_count, 2)
            print(f'Average price {current_year}: {avg_price}')

            year_price_sum = 0
            year_price_count = 0
            current_year = changed_list[i][2]

            year_price_sum += float(changed_list[i][3])
            year_price_count += 1

        if i == len(changed_list) - 1:
            avg_price = round(year_price_sum / year_price_count, 2)
            print(f'Average price {current_year}: {avg_price}')




def print_month_avg_price(changed_list):
    current_month = changed_list[0][0]
    month_price_sum = 0
    month_price_count = 0

    for i in range(len(changed_list)):

        if current_month == changed_list[i][0]:

            month_price_sum += float(changed_list[i][3])
            month_price_count += 1

        else:
            avg_price = round(month_price_sum / month_price_count, 2)
            print(f'Average price {current_month}: {avg_price}')

            month_price_sum = 0
            month_price_count = 0
            current_month = changed_list[i][0]

            month_price_sum += float(changed_list[i][3])
            month_price_count += 1

        if i == len(changed_list) - 1:
            avg_price = round(month_price_sum / month_price_count, 2)
            print(f'Average price {current_month}: {avg_price}')



def print_min_max_price(changed_list):
    current_year = changed_list[0][2]
    year_prices = []

    for i in range(len(changed_list)):

        if current_year == changed_list[i][2]:
            year_prices.append(float(changed_list[i][3]))
        else:
            print(min(year_prices))
            print(max(year_prices))
            year_prices = [float(changed_list[i][3])]
            current_year = changed_list[i][2]

        if i == len(changed_list) - 1:
            print(min(year_prices))
            print(max(year_prices))




def write_max_prices(changed_list):
    prices = [float(item[3]) for item in changed_list]

    with open('maxprices.txt', 'w', encoding='utf8') as num_file:
        prices.sort()
        for item in prices:
            num_file.write(str(item) + '\n')


def write_min_prices(changed_list):
    prices = [float(item[3]) for item in changed_list]

    with open('minprices.txt', 'w', encoding='utf8') as num_file:
        prices.reverse()
        for item in prices:
            num_file.write(str(item) + '\n')




changed_list = get_list()

print_year_avg_price(changed_list)
print_month_avg_price(changed_list)
print_min_max_price(changed_list)
write_max_prices(changed_list)
write_min_prices(changed_list)
