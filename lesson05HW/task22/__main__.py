# Словарный индекс. Напишите программу, которая читает содержимое текстового файла.
# Программа должна создать словарь, в котором пары ключ/значение описаны следующим образом:
# • ключ - ключами являются отдельные слова в файле;
# • значение - каждое значение является списком, который содержит номера строк
# в файле, где найдено слово (ключ).
# Например, предположим, что слово "робот" найдено в строках 7, 18, 94 и 138. Словарь
# будет содержать элемент, в котором ключом будет строковое значение "робот", а значением - список,
# содержащий номера 7, 18, 94 и 138.
# После создания словаря программа должна создать еще один текстовый файл, называемый словарным индексом,
# в котором приводится содержимое словаря. Словарный
# индекс должен содержать список слов в алфавитном порядке, хранящихся в словаре
# в качестве ключей, и номера строк, в которых эти слова встречаются в исходном файле.
# На рис. 9.1 показан пример исходного текстового файла (Kennedy.txt) и его индексного
# файла (index.txt).


def get_text(filename):
    with open(filename, 'r', encoding='utf8') as file:
        return file.read().lower().split('\n')


def write_words_indexes(data, filename):
    sorted_keys = sorted(dct)
    with open(filename, 'w', encoding='utf8') as file:
        for key in sorted_keys:
            file.write(f'{key}: {" ".join(data[key])}\n')


text_lines = get_text('text.txt')
dct = {}

for line_key in range(len(text_lines)):
    words = text_lines[line_key].replace(',', '').replace('.', '').split(' ')
    for word_key in range(len(words)):
        if words[word_key] in dct:
            dct[words[word_key]].append(str(line_key + 1))
        else:
            dct[words[word_key]] = [str(line_key + 1)]


write_words_indexes(dct, 'words-indexes.txt')

