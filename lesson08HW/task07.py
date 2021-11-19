# Допустим, что переменная data entry ссылается на элемент интерфейса Entry. Напишите инструкцию,
# которая извлекает значение из этого элемента, приводит его к типу int
# и присваивает его переменной с именем var.

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button_frame = tkinter.Frame(self.main_window)
        self.button = tkinter.Button(self.button_frame, text='show', command=self.get_entry)
        self.data_entry = tkinter.Entry(self.main_window, width=10)

        self.button_frame.pack(side='left')
        self.button.pack()
        self.data_entry.pack()

        tkinter.mainloop()

    def get_entry(self):
        var = int(self.data_entry.get())
        tkinter.messagebox.showinfo('title', var)


my_gui = MyGUI()