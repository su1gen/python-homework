# Сидячие места на стадионе. На стадионе имеется три категории сидячих мест. Места
# класса А стоят 20 долларов, места класса В - 15 долларов и места класса С - 1 О долларов. Н
# апишите программу, которая запрашивает, сколько билетов каждого класса было
# продано, и затем выводит сумму дохода, полученного за счет продажи билетов.

def count_value(amount, ticket_value):
    return ticket_value * amount


def main():
    a_tickets = int(input('Билеты класа А '))
    b_tickets = int(input('Билеты класа B '))
    c_tickets = int(input('Билеты класа C '))

    a_tickets_value = count_value(a_tickets, 20)
    b_tickets_value = count_value(b_tickets, 15)
    c_tickets_value = count_value(c_tickets, 10)

    summa = a_tickets_value + b_tickets_value + c_tickets_value

    print(f'Сумма дохода: {summa}')


if __name__ == '__main__':
    main()
