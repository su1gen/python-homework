# Частотность слов. Напишите программу, которая считывает содержимое текстового
# файла. Она должна создать словарь, в котором ключами являются отдельные слова
# в файле, и значениями - количество появлений каждого слова. Например, если слово
# 'это' появляется 128 раз, то словарь должен содержать элемент с ключом 'это' и значением 128.
# Программа должна либо показать частотность каждого слова, либо создать
# второй файл, содержащий список слов и их частотностей.


def get_words_amount(filename):
    with open(filename, 'r', encoding='utf8') as file:
        text = file.read().replace('\n', ' ').replace(',', '').replace('.', '')
        words_amount = {}

        for word in text.split(' '):
            if word in words_amount:
                words_amount[word] += 1
            else:
                words_amount[word] = 1

        return words_amount


print(get_words_amount('task15/text.txt'))


