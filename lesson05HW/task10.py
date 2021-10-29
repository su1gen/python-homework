# Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фрагмент кода,
# который создает еще одно множество с элементами, не принадлежащими
# одновременно setl и set2, и присвойте получившееся множество переменной setЗ.


set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9}

set3 = set2.symmetric_difference(set1)

print(set1, set2, set3)