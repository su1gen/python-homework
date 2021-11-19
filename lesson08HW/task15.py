# Междугородные звонки. Провайдер междугородних звонков взимает плату за телефонные вызовы в
# соответствии с приведенными в табл. 13 .13 тарифами.
# Напишите приложение с GUI, которое позволяет пользователю выбирать категорию
# уровня (из набора радиокнопок) и вводить в элемент интерфейса Entry продолжительность вызова в минутах.
# Информационное диалоговое окно должно выводить на экран
# стоимость вызова (рис. 13.48).


import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.check_frame = tkinter.Frame(self.main_window)
        self.minutes_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(10)

        self.rb1 = tkinter.Radiobutton(self.check_frame, text='Дневное время (с 6:00 до 17:59)', variable=self.radio_var, value=10)
        self.rb2 = tkinter.Radiobutton(self.check_frame, text='Вечернее время (с 18:00 до 23:59)', variable=self.radio_var, value=12)
        self.rb3 = tkinter.Radiobutton(self.check_frame, text='Непиковый период (с полуночи до 5:59) ', variable=self.radio_var, value=5)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.minutes_label = tkinter.Label(self.minutes_frame, text='Введите количество минут:')
        self.minutes_entry = tkinter.Entry(self.minutes_frame, width=10)

        self.minutes_label.pack(side='left')
        self.minutes_entry.pack(side='left')

        self.calc_button = tkinter.Button(self.buttons_frame, text='Показать стоимость',
                                          command=self.calculate)
        self.exit_button = tkinter.Button(self.buttons_frame, text='Выйти', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.check_frame.pack()
        self.minutes_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        value = float(self.radio_var.get())
        minutes = float(self.minutes_entry.get())
        tkinter.messagebox.showinfo('Baши затраты = ', round(value * minutes, 2))



my_gui = MyGUI()
