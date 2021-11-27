import tkinter
import tkinter.messagebox

from lesson09HW.classes.gui.galaxy_window import GalaxyWindow
from lesson09HW.classes.gui.planet_window import PlanetWindow
from lesson09HW.classes.gui.satellite_window import SatelliteWindow
from lesson09HW.controllers.galaxy_controller import GalaxyController
from lesson09HW.controllers.planet_controller import PlanetController
from lesson09HW.controllers.satellite_controller import SatelliteController


class MainWindow:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Main window")

        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        position_x = int((screen_width - 800) / 2)
        position_y = int((screen_height - 400) / 2)

        self.main_window.geometry(f"600x400+{position_x}+{position_y}")

        file_menu = tkinter.Menu()
        file_menu.add_command(label="Add Galaxy", command=self.open_galaxy)
        file_menu.add_command(label="Add Planet", command=self.open_planet)
        file_menu.add_command(label="Add Satellite", command=self.open_satellite)

        main_menu = tkinter.Menu()
        main_menu.add_cascade(label="Add space object", menu=file_menu)

        self.main_window.config(menu=main_menu)

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.frame1, text='Вывести  информацию  обо  всех  \nпланетах,  на  которых  '
                                                      'присутствует жизнь, \nи их спутниках в заданной галактике')
        self.entry1 = tkinter.Entry(self.frame1, width=30)
        self.button1 = tkinter.Button(self.frame1, text='Показать',
                                      command=self.get_planets_with_life_by_galaxy)

        self.label1.pack(side='left')
        self.entry1.pack(side='left')
        self.button1.pack(side='left')

        self.label2 = tkinter.Label(self.frame2, text='Вывести информацию о планетах и их \nспутниках, имеющих '
                                                      'наименьший радиус и \nнаибольшее количество спутников.')
        self.button2 = tkinter.Button(self.frame2, text='Показать',
                                      command=self.get_planest_with_min_radius)

        self.label2.pack(side='left')
        self.button2.pack(side='left')

        self.label3 = tkinter.Label(self.frame3, text='Вывести  информацию о планете, галактике, \nв которой она '
                                                      'находится, и ее спутниках, \nимеющей максимальное количество '
                                                      'спутников, но с наименьшим \nобщим объемом этих спутников.')
        self.button3 = tkinter.Button(self.frame3, text='Показать',
                                      command=self.get_planets_with_max_satellites)

        self.label3.pack(side='left')
        self.button3.pack(side='left')

        self.label4 = tkinter.Label(self.frame4, text='Найти галактику, сумма ядерных температур \n'
                                                      'планет которой наибольшая.')
        self.button4 = tkinter.Button(self.frame4, text='Показать',
                                      command=self.get_galaxy_with_max_core)

        self.label4.pack(side='left')
        self.button4.pack(side='left')

        self.frame1.pack(pady=10)
        self.frame2.pack(pady=10)
        self.frame3.pack(pady=10)
        self.frame4.pack(pady=10)

        self.main_window.mainloop()

    def get_planets_with_life_by_galaxy(self):
        galaxy_name = self.entry1.get()
        if galaxy_name:
            planet_controller = PlanetController()
            planets = planet_controller.get_planets_with_life_by_galaxy(galaxy_name)
            if len(planets) > 0:
                satellite_controller = SatelliteController()
                message = ''
                for planet in planets:
                    message += planet.__str__() + '\n'
                    satellites = satellite_controller.get_satellites_by_planet_id(planet.id)
                    if len(satellites) > 0:
                        for satellite in satellites:
                            message += satellite.__str__() + '\n'
                tkinter.messagebox.showinfo('Внимание', message)
            else:
                tkinter.messagebox.showinfo('Внимание', 'Нет планет!')
        else:
            tkinter.messagebox.showinfo('Внимание', 'Нужно ввести название галактики!')

    def get_planest_with_min_radius(self):
        planet_controller = PlanetController()
        planets = planet_controller.get_planets_with_min_radius()
        if len(planets) > 0:
            satellite_controller = SatelliteController()
            message = ''
            for planet in planets:
                message += planet.__str__() + '\n'
                satellites = satellite_controller.get_satellites_by_planet_id(planet.id)
                if len(satellites) > 0:
                    for satellite in satellites:
                        message += satellite.__str__() + '\n'
            tkinter.messagebox.showinfo('Внимание', message)
        else:
            tkinter.messagebox.showinfo('Внимание', 'Нет планет!')

    def get_planets_with_max_satellites(self):
        planet_controller = PlanetController()
        planet = planet_controller.get_planet_with_max_satellites()
        if planet:
            message = ''
            galaxy_controller = GalaxyController()
            galaxy = galaxy_controller.get_galaxy_by_id(planet.galaxy_id)
            message += galaxy.__str__() + '\n'
            message += planet.__str__() + '\n'
            satellite_controller = SatelliteController()
            satellites = satellite_controller.get_satellites_by_planet_id(planet.id)
            if len(satellites) > 0:
                for satellite in satellites:
                    message += satellite.__str__() + '\n'
            tkinter.messagebox.showinfo('Внимание', message)
        else:
            tkinter.messagebox.showinfo('Внимание', 'Нет планет!')

    def get_galaxy_with_max_core(self):
        galaxy_controller = GalaxyController()
        galaxy = galaxy_controller.get_galaxy_with_max_core()
        if galaxy:
            tkinter.messagebox.showinfo('Внимание', galaxy.__str__())
        else:
            tkinter.messagebox.showinfo('Внимание', 'Нет галактик!')


    def open_galaxy(self):
        GalaxyWindow()

    def open_planet(self):
        PlanetWindow()

    def open_satellite(self):
        SatelliteWindow()


if __name__ == '__main__':
    my_win = MainWindow()
