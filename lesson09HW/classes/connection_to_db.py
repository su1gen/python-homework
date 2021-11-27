import sqlite3


class ConnectionToDB:
    def __init__(self):
        self.__connection_to_db = sqlite3.connect('../../space.sqlite')

    def get_connection(self):
        return self.__connection_to_db

    def disconnect_from_db(self):
        self.__connection_to_db.close()