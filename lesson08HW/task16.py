# Рисунок старого дома. Примените элемент интерфейса Canvas, с которым вы познакомились в этой главе,
# чтобы нарисовать дом. Рисунок дома должен содержать по меньшей
# мере два окна и дверь. Можно добавить и другие объекты, такие как небо, солнце и даже
# облака (рис. 13.49).

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.main_window, width=1000, height=700)

        self.canvas.create_rectangle(50, 250, 950, 690)
        self.canvas.create_rectangle(100, 300, 300, 440)
        self.canvas.create_rectangle(700, 300, 900, 440)
        self.canvas.create_rectangle(400, 300, 600, 690)

        self.canvas.create_polygon(25, 250, 975, 250, 500, 50, 25, 250)

        self.canvas.create_oval(900, 25, 950, 75)


        self.canvas.pack()
        tkinter.mainloop()


my_gui = MyGUI()