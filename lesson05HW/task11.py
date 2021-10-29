# Предположим, что переменная dct ссылается на словарь. Напишите фрагмент кода, который
# консервирует словарь и сохраняет его в файле mydata.dat.

import pickle

dct = {
    'a': 1,
    'b': 2,
    'c': 3,
    'James': 4,
    'Jim': 5,
}

with open('mydata.dat', 'wb') as file:
    pickle.dump(dct, file)

    