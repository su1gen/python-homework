# Предположим, что переменная dct ссылается на словарь. Напишите инструкцию if, которая определяет,
# существует ли в словаре ключ 'Джеймс'. Если да, то покажите значение, которое связано с этим ключом.
# Если ключа в словаре нет, то покажите соответствующее сообщение.


dct = {
    'a': 1,
    'b': 2,
    'c': 3,
}

if 'James' in dct:
    print(dct.get('James'))
else:
    print('no')