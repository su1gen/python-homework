# Калькулятор миль на галлон бензина. Напишите программу с GUI, которая вычисляет
# экономичность автомобиля. Окно программы должно содержать элементы интерфейса
# Entry, которые позволяют пользователю вводить объем бензина в галлонах, заправленного в автомобиль,
# и количество миль, которые он может пройти с полным баком
# (рис. 13.44). При нажатии кнопки Вычислить MGP программа должна вывести на экран
# количество миль, которые автомобиль может пройти в расчете на галлон бензина.
# Для вычисления показателя количества миль на галлон примените приведенную ниже
# формулу:
# Показатель миль на галлоны = мили / галлоны

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.answer_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        self.gallons_label = tkinter.Label(self.gallons_frame, text='Введите количестео галлонов:')
        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=10)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.miles_label = tkinter.Label(self.miles_frame, text='Введите количество миль:')
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.answer = tkinter.StringVar()
        self.answer_label = tkinter.Label(self.answer_frame, text='Мили на галлон (MPG) = ')
        self.answer_content = tkinter.Label(self.answer_frame, textvariable=self.answer)
        self.answer_label.pack(side='left')
        self.answer_content.pack(side='left')

        self.calc_button = tkinter.Button(self.buttons_frame, text='Вычислить MGP', command=self.calculate)
        self.exit_button = tkinter.Button(self.buttons_frame, text='Выйти', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.answer_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        self.answer.set(round(float(self.miles_entry.get()) / float(self.gallons_entry.get()), 2))


my_gui = MyGUI()
