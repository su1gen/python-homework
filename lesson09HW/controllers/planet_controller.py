from lesson09HW.classes.connection_to_db import ConnectionToDB
from lesson09HW.classes.planet import Planet


class PlanetController:

    def add_planet(self, planet):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'INSERT INTO Planets (name, radius, core_temperature, has_atmosphere, has_life, galaxy_id) '
                       f'VALUES ("{planet.name}", "{planet.radius}", "{planet.core_temperature}", '
                       f'"{planet.has_atmosphere}", "{planet.has_life}", "{planet.galaxy_id}")')
        current_connection.commit()
        connection_to_db.disconnect_from_db()

    def get_planets(self):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * FROM Planets')
        planets = [Planet(item[1], item[2], item[3], item[4], item[5], item[6], id=item[0]) for item in cursor.fetchall()]
        connection_to_db.disconnect_from_db()
        return planets

    def get_planets_with_life_by_galaxy(self, galaxy_name):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * FROM Planets INNER JOIN Galaxies ON Planets.galaxy_id = Galaxies.id '
                       f'WHERE Galaxies.name = "{galaxy_name}" AND Planets.has_life = 1')
        planets = [Planet(item[1], item[2], item[3], item[4], item[5], item[6], id=item[0]) for item in cursor.fetchall()]
        connection_to_db.disconnect_from_db()
        return planets

    def get_planets_with_min_radius(self):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * FROM Planets WHERE radius = (select min(radius)from Planets)')
        planets = [Planet(item[1], item[2], item[3], item[4], item[5], item[6], id=item[0]) for item in cursor.fetchall()]
        connection_to_db.disconnect_from_db()
        return planets

    def get_planet_with_max_satellites(self):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * FROM Satellites GROUP BY planet_id ORDER BY count(planet_id) DESC LIMIT 1')
        satellite = cursor.fetchall()
        cursor.execute(f'SELECT * FROM Planets WHERE id = {satellite[0][3]}')
        planet = cursor.fetchall()
        connection_to_db.disconnect_from_db()
        return Planet(planet[0][1], planet[0][2], planet[0][3], planet[0][4], planet[0][5], planet[0][6], id=planet[0][0])


