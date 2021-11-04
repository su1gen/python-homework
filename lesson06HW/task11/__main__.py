# Класс cashReqi.ster. Это упражнение предполагает создание класса Retailitem из задачи 5 по программированию.
# Создайте класс CashRegister (Кассовый аппарат), который
# может использоваться вместе с классом Retailitem. Класс cashRegister должен иметь
# внутренний список объектов Retailitem, а также приведенные ниже методы.
# • Метод purchase _ item () (приобрести товар) в качестве аргумента принимает объект
# Retailrtem. При каждом вызове метода purchase_item() объект Retailrtem, переданный в качестве аргумента,
# должен быть добавлен в список.
# • Метод get _ total () (получить сумму покупки) возвращает общую стоимость всех
# объектов Retailrtem, хранящихся во внутреннем списке объекта CashRegister.
# • Метод show items () (показать товары) выводит данные об объектах Retailrtem,
# хранящихся во внутреннем списке объекта cashRegister.
# • Метод clear () (очистить) должен очистить внутренний список объекта CashRegister.
# Продемонстрируйте класс CashRegister в программе, которая позволяет пользователю
# выбрать несколько товаров для покупки. Когда пользователь готов рассчитаться за покупку,
# программа должна вывести список всех товаров, которые он выбрал для покупки,
# а также их общую стоимость.

from lesson06HW.task08.retailitem import RetailItem
from lesson06HW.task11.cash_register import CashRegister

if __name__ == '__main__':

    cash_register = CashRegister()

    for i in range(3):
        description = input('Enter description ')
        amount = int(input('Enter amount '))
        price = float(input('Enter price '))

        retail_item = RetailItem(description, amount, price)
        cash_register.purchase_item(retail_item)

    cash_register.show_items()
    print(cash_register.get_total())

