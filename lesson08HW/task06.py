# Напишите инструкцию, которая создает элемент интерфейса Button, закрывающий
# программу при его нажатии. Его родительским элементом должен быть элемент
# se l f . bu t ton _ f r ame, и он должен содержать текст ' Выйти' .

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button_frame = tkinter.Frame(self.main_window)
        self.button = tkinter.Button(self.button_frame, text='Выйти', command=self.main_window.destroy)

        self.button_frame.pack(side='left')
        self.button.pack()

        tkinter.mainloop()


my_gui = MyGUI()