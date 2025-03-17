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
                        escapeTime TEXT "00:00")''')
        connection.commit()
        connection.close()
    
def insertData(request):
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO players (name, surname, email, phone, escapeTime) VALUES (?, ?, ?, ?,?)',
                       (name, surname, email, phone, "15:00"))
    connection.commit()
    connection.close()

def updateData(escapeTime):
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('UPDATE players SET escapeTime = ? WHERE id = (SELECT MAX(id) FROM players);',
                   (escapeTime,))
    connection.commit()
    connection.close()

    return jsonify({'message': 'Time recorded successfully'})

def retrieveData():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT name || ' ' || surname AS 'username', email, phone, escapeTime FROM players ORDER BY escapeTime;")
    users = cursor.fetchall()
    connection.close()
    return users

def ThreeTopData():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT name || ' ' || surname AS 'username', escapeTime FROM players ORDER BY escapeTime LIMIT 3;")
    users = cursor.fetchall()
    connection.close()
    return users

def databaseCheck():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()

    # Retrieve and print all player records
    cursor.execute("SELECT COUNT(*) FROM players")
    qty = cursor.fetchall()
    cursor.execute("SELECT name || ' ' || surname AS 'username', escapeTime FROM players ORDER BY escapeTime;")
    rows = cursor.fetchall()

    print(f"Total Rows: {qty[0]}")
    for row in rows:
        print(row)  # Prints each record

    connection.close()

if __name__ == '__main__':
    databaseCheck()