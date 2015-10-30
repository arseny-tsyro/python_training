__author__ = 'Arseniy'
import mysql.connector


class DbFixture:
    def __init__(self, name, host, user, password):
        self.name = name
        self.host = host
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def destroy(self):
        self.connection.close()