class CashRegister:
    def __init__(self):
        self.__retail_item_list = []

    def purchase_item(self, retail_item):
        self.__retail_item_list.append(retail_item)

    def get_total(self):
        return sum([item.get_price() * item.get_amount() for item in self.__retail_item_list])

    def show_items(self):
        for item in self.__retail_item_list:
            print(item)

    def clear(self):
        self.__retail_item_list.clear()
