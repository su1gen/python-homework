from lesson07HW.task06.classes.customer import Customer
import operator


class CustomersList:
    def __init__(self):
        self.__customers = list()

    def add(self, customer):
        self.__customers.append(customer)

    def get_sorted_customers_by_surname(self):
        sorted_customers = sorted(self.__customers, key=operator.attrgetter('surname'))
        return [customer.__str__() for customer in sorted_customers]

    def get_customers_in_credit_card_range(self, min, max):
        return [customer.__str__() for customer in self.__customers if min <= customer.credit_card <= max]

    def get_customers_dict(self):
        return [customer.to_dict() for customer in self.__customers]

    def get_customers_from_dict(self, data):
        for customer in data:
            self.__customers.append(
                Customer(customer['id'], customer['surname'], customer['name'], customer['patronymic'],
                         customer['address'], customer['phone'], customer['credit_card'], customer['bank_account']))





