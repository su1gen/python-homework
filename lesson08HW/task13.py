# Налоr на недвижимость. Территориальный округ собирает налоги на недвижимое имущество,
# опираясь на оценочную стоимость имущества, которая составляет 60% фактической стоимости недвижимого имущества.
# Если акр земли оценивается в $1 О ООО, то его
# оценочная стоимость составляет $6000. Налог на имущество в таком случае составит
# $0. 75 для каждого $100 оценочной стоимости. Налог на акр, оцененный в $6000, составит
# $45.00. Напишите программу с GUI, которая выводит на экран оценочную стоимость
# и налог на недвижимое имущество при вводе пользователем фактической стоимости
# недвижимого имущества (рис. 13.46).

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.amount_frame = tkinter.Frame(self.main_window)
        self.answer1_frame = tkinter.Frame(self.main_window)
        self.answer2_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        self.amount_label = tkinter.Label(self.amount_frame, text='Введите стоимость имущества: $')
        self.amount_entry = tkinter.Entry(self.amount_frame, width=10)
        self.amount_label.pack(side='left')
        self.amount_entry.pack(side='left')

        self.answer1 = tkinter.StringVar()
        self.answer1_label = tkinter.Label(self.answer1_frame, text='Оценочная стоимость: $')
        self.answer1_content = tkinter.Label(self.answer1_frame, textvariable=self.answer1)
        self.answer1_label.pack(side='left')
        self.answer1_content.pack(side='left')

        self.answer2 = tkinter.StringVar()
        self.answer2_label = tkinter.Label(self.answer2_frame, text='Налог на имущество: $')
        self.answer2_content = tkinter.Label(self.answer2_frame, textvariable=self.answer2)
        self.answer2_label.pack(side='left')
        self.answer2_content.pack(side='left')

        self.calc_button = tkinter.Button(self.buttons_frame, text='Вычислить',
                                          command=self.calculate)
        self.exit_button = tkinter.Button(self.buttons_frame, text='Выйти', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.amount_frame.pack()
        self.answer1_frame.pack()
        self.answer2_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def calculate(self):

        price = round(float(self.amount_entry.get()) * 0.6, 2)

        self.answer1.set(price)
        self.answer2.set(round(price * 0.0075, 2))


my_gui = MyGUI()