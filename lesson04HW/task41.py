# Разделитель слов. Напишите программу, которая на входе принимает предложение,
# в котором все слова написаны без пробелов, но первая буква каждого слова находится
# в верхнем регистре. Преобразуйте предложение в строковое значение, в котором слова
# отделены пробелами, и только первое слово начинается с буквы в верхнем регистре. Например, строковое значение
# "ОстановисьИПочувствуйЗапахРоз" будет преобразовано
# в "Остановись и почувствуй запах з".

string = input("Enter text ")
current_word = ''
word_list = []

for i in range(len(string)):
    if (string[i].isupper() and i != 0):
        word_list.append(current_word)
        current_word = ''

    current_word += string[i].lower()

    if i == len(string) - 1:
        word_list.append(current_word)

new_string = ' '.join(word_list).capitalize()

print(new_string)
