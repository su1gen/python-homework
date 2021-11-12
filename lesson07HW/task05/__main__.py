# Классы Person и Custaaer. Напишите класс Person с атрибутами данных для имени, адреса и телефонного номера
# человека. Затем напишите класс Custorner (Клиент), который является подклассом класса
# Person. Класс Custorner должен иметь атрибут данных для номера клиента и атрибут
# булевых данных, указывающий, хочет ли клиент быть в списке рассылки или нет. Продемонстрируйте экземпляр класса
# Custorner в простой программе.

from lesson07HW.task05.customer import Customer

if __name__ == '__main__':
    name = input('Enter name ')
    number = input('Enter number ')
    phone = input('Enter phone ')
    client_num = input('Enter client number ')
    is_subscribed = input("Enter is subscribed (0/1) ")

    supervisor = Customer(name, number, phone, client_num, is_subscribed)

    print(supervisor)
