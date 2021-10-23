# 1. Прочитать из файла info.json данные в dict
# 2. Отобразить количество хобби сотрудника и вывести их на екран
# 3. Сколько детей у сотрудника
# 4. Вывести имя старшего ребенка
# 5. Добавить в dict сотрудника ключ "email": jane@company.com , "phone": 123456
# и сохранить в новый файл info2.json

import json


def get_data(filename='info.json'):
    with open(filename, 'r') as file:
        return json.load(file)


def show_hobbies(data):
    if 'hobbies' in data:
        print(f'Hobbies amount: {len(data["hobbies"])}')
        for hobby in data["hobbies"]:
            print(hobby)
    else:
        print(f'No hobbies')


def show_children_amount(data):
    if 'children' in data:
        print(f'Children: {len(data["children"])}')
    else:
        print(f'No children')


def show_oldest_child(data):
    if 'children' in data and len(data['children']) > 0:
        oldest = data['children'][0]
        for child in data['children']:
            if oldest['age'] < child['age']:
                oldest = child
        print(f'Oldest child is {oldest["firstName"]}')


def add_field(data, key, value):
    data[key] = value


def write_data(data, filename='info2.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    file_data = get_data()
    show_hobbies(file_data)
    show_children_amount(file_data)
    show_oldest_child(file_data)
    add_field(file_data, 'email', 'jane@company.com')
    add_field(file_data, 'phone', '123456')
    write_data(file_data, filename='info2.json')
