# Анализ файла. Напишите программу, которая читает содержимое двух текстовых файлов и сравнивает их следующим образом:
# • показывает список всех уникальных слов, содержащихся в обоих файлах;
# • показывает список слов, входящих в оба файла;
# • показывает список слов из первого файла, не входящих во второй;
# • показывает список слов из второго файла, не входящих в первый;
# • показывает список слов, входящих либо в первый, либо во второй файл, но не входящих в оба файла одновременно.
# Подсказка: для выполнения этого анализа используйте операции над множествами.


def get_words(filename):
    with open(filename, 'r', encoding='utf8') as file:
        text = file.read().replace('\n', ' ').replace(',', '').replace('.', '')
        return set(text.split(' '))


words1 = get_words('text1.txt')
words2 = get_words('text2.txt')

all_words = words1.union(words2)
inter_wards = words1.intersection(words2)
word1_diff = words1.difference(words2)
word2_diff = words2.difference(words1)
unique_words = words1.symmetric_difference(words2)

print(all_words, inter_wards, word1_diff, word2_diff, unique_words, sep='\n')
