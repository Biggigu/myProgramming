import sqlite3
from flask import jsonify,request

class DatabaseConnection:
    def __init__(self, database_file="database.db"):
        self.database_file = database_file
        self.newDBIfNoExist()

    def connect(self):
        connection = sqlite3.connect(self.database_file)
        return connection
    
    def newDBIfNoExist(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        surname TEXT,
                        email TEXT,
                        phone TEXT,
                        escapeTime TEXT)''')
        connection.commit()
        connection.close()
    
def insertData(request):
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO players (name, surname, email, phone) VALUES (?, ?, ?, ?)',
                       (name, surname, email, phone))
    connection.commit()
    connection.close()

def updateData(name,surname,escapeTime):
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('UPDATE players SET escapeTime = ? WHERE name = ? AND surname = ?',
                   (escapeTime, name, surname))
    connection.commit()
    connection.close()

    return jsonify({'message': 'Time recorded successfully'})

def retrieveData():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('SELECT name || " " || surname, escapeTime FROM players ORDER BY escapeTime ASC LIMIT 10')
    data = [{'username': row[0], 'time': row[1]} for row in cursor.fetchall()]
    connection.close()
    return jsonify(data)