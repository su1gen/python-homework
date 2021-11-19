import tkinter
import tkinter.messagebox
from tkinter import messagebox, END

from lesson08HW.task17.classes.amfibia import Amfibia
from lesson08HW.task17.classes.bat_mobile import BatMobile
from lesson08HW.task17.classes.car import Car
from lesson08HW.task17.classes.plane import Plane
from lesson08HW.task17.classes.ship import Ship
from lesson08HW.task17.classes.vehicle_list import VehicleList


class MyGUI:
    def __init__(self):

        self.car1 = Car(1000, 200, 2003)
        self.car2 = Car(5000, 300, 2020)
        self.car3 = Car(3000, 400, 2009)
        self.plane1 = Plane(10000, 400, 2009, 30, 300)

        self.vehicle_list1 = VehicleList()
        self.vehicle_list1.add(self.car1)
        self.vehicle_list1.add(self.car2)
        self.vehicle_list1.add(self.car3)
        self.vehicle_list1.add(self.plane1)

        self.bat1 = BatMobile(1000, 200, 2003)
        self.amf1 = Amfibia(5000, 300, 2020)
        self.ship1 = Ship(3000, 400, 2009, 500, 'Odessa')
        self.plane2 = Plane(11000, 400, 2008, 30, 300)
        self.car4 = Car(10000, 400, 2021)

        self.vehicle_list2 = VehicleList()
        self.vehicle_list2.add(self.bat1)
        self.vehicle_list2.add(self.amf1)
        self.vehicle_list2.add(self.ship1)
        self.vehicle_list2.add(self.plane2)
        self.vehicle_list2.add(self.car4)

        self.car5 = Car(1000, 200, 2003)
        self.car6 = Car(5000, 300, 2020)
        self.plane3 = Plane(10000, 400, 2009, 30, 300)
        self.ship2 = Ship(10000, 400, 2009, 30, 300)

        self.vehicle_list3 = VehicleList()
        self.vehicle_list3.add(self.car5)
        self.vehicle_list3.add(self.car6)
        self.vehicle_list3.add(self.plane3)
        self.vehicle_list3.add(self.ship2)

        self.main_window = tkinter.Tk()

        self.button1 = tkinter.Button(self.main_window, text='вывести на екран механизм с наибольшей ценой',
                                      command=self.get_most_expensive_vehicle)
        self.button2 = tkinter.Button(self.main_window, text='получить механизм с наименьшей ценой',
                                      command=self.get_cheapest_vehicle)
        self.button3 = tkinter.Button(self.main_window, text='получить механизм с ценой меньше 10000 после 2000 года',
                                      command=self.get_vehicles_cheaper_than_after_year)
        self.button4 = tkinter.Button(self.main_window, text='получить масив механизмов год выпуска с 2000 по 2010',
                                      command=self.get_vehicles_between_years)
        self.button5 = tkinter.Button(self.main_window,
                                      text='получить масив механизмов не старше 5 лет с средней ценой(+- 20%) и '
                                           'скоростью в диапазоне от 100 до 200',
                                      command=self.get_vehicles_not_older_average_price_between_speed)
        self.button6 = tkinter.Button(self.main_window, text='в масиве механизмов получить количество Car и Plane',
                                      command=self.get_amount_of_cars_and_planes)
        self.button7 = tkinter.Button(self.main_window, text='получить из масива механизмов Car с наименьшей ценой',
                                      command=self.get_cheapest_car)
        self.button8 = tkinter.Button(self.main_window, text='получить из масива механизмов масив Ship год выпуска с '
                                                             '2000 по 2010',
                                      command=self.get_ships_between_years)
        self.button9 = tkinter.Button(self.main_window, text='подсчитать среднюю цену',
                                      command=self.get_average_price)
        self.button10 = tkinter.Button(self.main_window, text='подсчитать максимальную скорость',
                                      command=self.get_max_speed)
        self.button11 = tkinter.Button(self.main_window, text='подсчитать минимальный год выпуска',
                                      command=self.get_min_year)

        self.listbox = tkinter.Listbox()

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()
        self.button7.pack()
        self.button8.pack()
        self.button9.pack()
        self.button10.pack()
        self.button11.pack()
        self.listbox.pack()

        tkinter.mainloop()

    def get_most_expensive_vehicle(self):
        # messagebox.showinfo("Title", self.vehicle_list1.get_most_expensive_vehicle())
        self.listbox.delete(0, END)
        self.listbox.insert(END, self.vehicle_list1.get_most_expensive_vehicle())

    def get_cheapest_vehicle(self):
        # messagebox.showinfo("Title", self.vehicle_list2.get_cheapest_vehicle())
        self.listbox.delete(0, END)
        self.listbox.insert(END, self.vehicle_list2.get_cheapest_vehicle())

    def get_vehicles_cheaper_than_after_year(self):
        # messagebox.showinfo("Title", self.vehicle_list3.get_vehicles_cheaper_than_after_year(10000, 2000))
        self.listbox.delete(0, END)
        for item in self.vehicle_list3.get_vehicles_cheaper_than_after_year(10000, 2000):
            self.listbox.insert(END, item)

    def get_vehicles_between_years(self):
        # messagebox.showinfo("Title", self.vehicle_list1.get_vehicles_between_years(2000, 2010))
        self.listbox.delete(0, END)
        for item in self.vehicle_list1.get_vehicles_between_years(2000, 2010):
            self.listbox.insert(END, item)

    def get_vehicles_not_older_average_price_between_speed(self):
        # messagebox.showinfo("Title", self.vehicle_list2.get_vehicles_not_older_average_price_between_speed(5, 4000, 100, 200))
        self.listbox.delete(0, END)
        for item in self.vehicle_list2.get_vehicles_not_older_average_price_between_speed(5, 4000, 100, 200):
            self.listbox.insert(END, item)

    def get_amount_of_cars_and_planes(self):
        # messagebox.showinfo("Title", self.vehicle_list3.get_amount_of_cars_and_planes())
        self.listbox.delete(0, END)
        self.listbox.insert(END, self.vehicle_list3.get_amount_of_cars_and_planes())

    def get_cheapest_car(self):
        # messagebox.showinfo("Title", self.vehicle_list1.get_cheapest_car())
        self.listbox.delete(0, END)
        self.listbox.insert(END, self.vehicle_list1.get_cheapest_car())

    def get_ships_between_years(self):
        # messagebox.showinfo("Title", self.vehicle_list2.get_ships_between_years(2000, 2010))
        self.listbox.delete(0, END)
        for item in self.vehicle_list2.get_ships_between_years(2000, 2010):
            self.listbox.insert(END, item)

    def get_average_price(self):
        # messagebox.showinfo("Title", self.vehicle_list3.get_avg_price())
        self.listbox.delete(0, END)
        self.listbox.insert(END, self.vehicle_list3.get_avg_price())

    def get_max_speed(self):
        # messagebox.showinfo("Title", self.vehicle_list3.get_max_speed())
        self.listbox.delete(0, END)
        self.listbox.insert(END, self.vehicle_list3.get_max_speed())

    def get_min_year(self):
        # messagebox.showinfo("Title", self.vehicle_list3.get_min_year())
        self.listbox.delete(0, END)
        self.listbox.insert(END, self.vehicle_list3.get_min_year())

