# Из шкалы Цельсия в шкалу Фаренгейта. Напишите программу с GUI, которая преобразует показания
# температуры по шкале Цельсия в температуру по шкале Фаренгейта.
# Пользователь должен иметь возможность вводить температуру по шкале Цельсия, нажимать кнопку и
# затем получать эквивалентную температуру по шкале Фаренгейта
# (рис. 13.45). Для выполнения этого преобразования примените приведенную ниже формулу:
# F=9/5*C+32,
# где F - это температура по Фаренгейту; С - температура по шкале Цельсия.

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.degree_frame = tkinter.Frame(self.main_window)
        self.answer_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        self.degree_label = tkinter.Label(self.degree_frame, text='Введите температуру в градусах Цельсия: ')
        self.degree_entry = tkinter.Entry(self.degree_frame, width=10)
        self.degree_label.pack(side='left')
        self.degree_entry.pack(side='left')

        self.answer = tkinter.StringVar()
        self.answer_label = tkinter.Label(self.answer_frame, text='Температура по шкале Фаренгейта: ')
        self.answer_content = tkinter.Label(self.answer_frame, textvariable=self.answer)
        self.answer_label.pack(side='left')
        self.answer_content.pack(side='left')

        self.calc_button = tkinter.Button(self.buttons_frame, text='Преобразовать в градусы Фаренгейта', command=self.calculate)
        self.exit_button = tkinter.Button(self.buttons_frame, text='Выйти', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.degree_frame.pack()
        self.answer_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        self.answer.set(round(9 / 5 * float(self.degree_entry.get()) + 32, 2))


my_gui = MyGUI()
