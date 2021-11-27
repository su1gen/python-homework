import tkinter
import tkinter.messagebox

from lesson09HW.classes.connection_to_db import ConnectionToDB
from lesson09HW.classes.galaxy import Galaxy
from lesson09HW.controllers.galaxy_controller import GalaxyController


class GalaxyWindow(tkinter.Toplevel):
    def __init__(self):
        self.galaxy_window = tkinter.Tk()
        self.galaxy_window.title("Galaxy window")

        screen_width = self.galaxy_window.winfo_screenwidth()
        screen_height = self.galaxy_window.winfo_screenheight()
        position_x = int((screen_width - 400) / 2)
        position_y = int((screen_height - 100) / 2)

        self.galaxy_window.geometry(f"400x100+{position_x}+{position_y}")

        self.name_frame = tkinter.Frame(self.galaxy_window)

        self.name_label = tkinter.Label(self.name_frame, text='Введите название галактики: ')
        self.name_entry = tkinter.Entry(self.name_frame, width=30)
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.save_button = tkinter.Button(self.galaxy_window, text='Добавить',
                                          command=self.save_galaxy)
        self.name_frame.pack(pady=20)
        self.save_button.pack()

        self.galaxy_window.mainloop()


    def save_galaxy(self):
        galaxy = Galaxy(self.name_entry.get())
        galaxy_controller = GalaxyController()
        galaxy_controller.add_galaxy(galaxy)

        tkinter.messagebox.showinfo('Внимание', 'Галактика успешно сохранена!' )


if __name__ == '__main__':
    GalaxyWindow()


