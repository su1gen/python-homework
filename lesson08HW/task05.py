# Напишите инструкцию, которая создает элемент интерфейса Button. Его родительским
# элементом должен быть self .button_frame, его текст должен содержать строковый
# литерал 'вычислить ', и его функцией обратного вызова должен быть метод
# self. calculate ().

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button_frame = tkinter.Frame(self.main_window)
        self.button = tkinter.Button(self.button_frame, text='вычислить', command=self.calculate)

        self.button_frame.pack(side='left')
        self.button.pack()

        tkinter.mainloop()

    def calculate(self):
        tkinter.messagebox.showinfo('Программа приостановлена', 'Нажмите ОК, когда будете готовы продолжить')


my_gui = MyGUI()