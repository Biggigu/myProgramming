import sqlite3

class DatabaseConnection:
    def __init__(self, database_file="escapeRoom.db"):
        self.database_file = database_file
        self.newDBIfNoExist()

    def connect(self):
        connection = sqlite3.connect(self.database_file)
        return connection
    
    def newDBIfNoExist(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS timeSlots (
                        bookingDate VARCHAR(50),
                        bookingTime VARCHAR(50))
                        username VARCHAR(50);''')
        connection.commit()
        connection.close()