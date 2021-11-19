# ФИО и адрес. Напишите программу с GUI, которая при нажатии кнопки выводит на
# экран ваше полное имя и адрес. При запуске программы ее окно должно выглядеть так,
# как на эскизе с левой стороны рис. 13.42. Когда пользователь нажимает кнопку Показать
# инфо, программа должна вывести на экран ваше имя и адрес, как показано на эскизе справа.


import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button_frame = tkinter.Frame(self.main_window)
        self.button1 = tkinter.Button(self.button_frame, text='Показать инфо', command=self.show_data)
        self.button2 = tkinter.Button(self.button_frame, text='Выйти', command=self.main_window.destroy)
        self.value = tkinter.StringVar()
        self.label = tkinter.Label(self.main_window, textvariable=self.value)

        self.label.pack()
        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button_frame.pack()



        tkinter.mainloop()

    def show_data(self):
        self.value.set('162390, Россия Вологодская обл,\n г. Великий Устюг.\n Почта Деда Мороза')


my_gui = MyGUI()