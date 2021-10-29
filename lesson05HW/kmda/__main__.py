# Проанализировать зарплаты КМДА csv файлы за 2019 год найти средние минимальные максимальные построить график


import matplotlib.pyplot as plt


def get_data(filename):
    with open(filename, 'r', encoding='utf8') as file:
        data = {}
        file.readline()
        for row in file:
            row_array = row.rstrip().split(';')
            data[row_array[0]] = float(row_array[9].replace('₴', '').replace(' ', '').replace(',', '.'))
        return data


def draw_diagram(data):
    left_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    bar_width = 10

    plt.bar(left_edges, data.values(), bar_width, color=('r', 'g', 'b', 'm', 'k'))

    plt.xlabel('Сотрудник')

    plt.ylabel('Зарплата')

    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80], data.keys())
    plt.xticks(rotation=90)
    #
    plt.yticks([0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000])

    plt.subplots_adjust(bottom=0.4)
    plt.show()


if __name__ == '__main__':
    data = get_data('berezen-2019.csv')
    salaries = data.values()

    max_salary = max(salaries)
    min_salary = min(salaries)
    average_salary = round(sum(salaries) / len(salaries), 2)

    print(max_salary, min_salary, average_salary)

    draw_diagram(data)

