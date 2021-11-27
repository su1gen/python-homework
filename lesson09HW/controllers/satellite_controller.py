from lesson09HW.classes.connection_to_db import ConnectionToDB
from lesson09HW.classes.satellite import Satellite


class SatelliteController:

    def add_satellite(self, satellite):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'INSERT INTO Satellites (name, distance, planet_id) '
                       f'VALUES ("{satellite.name}", "{satellite.distance}", "{satellite.planet_id}")')
        current_connection.commit()
        connection_to_db.disconnect_from_db()

    def get_satellites(self):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * FROM Satellites')
        satellites = [Satellite(item[1], item[2], item[3], id=item[0]) for item in cursor.fetchall()]
        connection_to_db.disconnect_from_db()
        return satellites

    def get_satellites_by_planet_id(self, planet_id):
        connection_to_db = ConnectionToDB()
        current_connection = connection_to_db.get_connection()
        cursor = current_connection.cursor()
        cursor.execute(f'SELECT * from Satellites WHERE planet_id = {planet_id}')

        satellites = [Satellite(item[1], item[2], item[3], id=item[0]) for item in cursor.fetchall()]
        connection_to_db.disconnect_from_db()
        return satellites