# Уникальные слова. Напишите программу, которая открывает заданный текстовый файл
# и затем показывает список всех уникальных слов в файле. (Подсказка: храните слова
# в качестве элементов множества.)


def get_unique_words(filename):
    with open(filename, 'r', encoding='utf8') as file:
        text = file.read().replace('\n', ' ').replace(',', '').replace('.', '')
        return set(text.split(' '))


print(get_unique_words('task15/text.txt'))