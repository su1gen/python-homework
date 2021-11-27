from lesson09HW.classes.connection_to_db import ConnectionToDB
from lesson09HW.classes.galaxy import Galaxy


class GalaxyController:

    def add_galaxy(self, galaxy):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'INSERT INTO Galaxies (name) VALUES ("{galaxy.name}")')
        current_connection.commit()
        connection_to_db.disconnect_from_db()

    def get_galaxies(self):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * FROM Galaxies')
        galaxies = [Galaxy(item[1], id=item[0]) for item in cursor.fetchall()]
        connection_to_db.disconnect_from_db()
        return galaxies

    def get_galaxy_by_id(self, galaxy_id):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * FROM Galaxies WHERE id = {galaxy_id}')
        galaxy = cursor.fetchall()
        connection_to_db.disconnect_from_db()
        return Galaxy(galaxy[0][1], id=galaxy[0][0])

    def get_galaxy_with_max_core(self):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT id, name, total_core FROM Galaxies u JOIN (SELECT galaxy_id, sum(core_temperature) as '
                       f'total_core from Planets GROUP  BY galaxy_id) AS t ON u.id = t.galaxy_id '
                       f'ORDER BY total_core DESC LIMIT 1')
        galaxy = cursor.fetchall()
        connection_to_db.disconnect_from_db()
        return Galaxy(galaxy[0][1], id=galaxy[0][0])
