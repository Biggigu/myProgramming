import sqlite3
from flask import jsonify,request

class DatabaseConnection:
    def __init__(self, database_file="data.db"):
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
                        idCard TEXT,
                        name TEXT,
                        surname TEXT,
                        email TEXT,
                        phone TEXT,
                        escapeTime TEXT)''')
        connection.commit()
        connection.close()
    
def checkUnique(value):
    value = value.upper()

    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM players WHERE idCard = ?', (value,))
    count = cursor.fetchone()[0]
    connection.close()
    return count == 0 # True if unique

def insertData(request):
    idCard = request.form.get('idCard')
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    
    idCard =idCard.upper()
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO players (idCard, name, surname, email, phone, escapeTime) VALUES (?,?,?,?,?,?)',
                       (idCard, name, surname, email, phone, "30:00"))
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

def retrieveOne():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT name || ' ' || surname AS 'username', email, phone, escapeTime FROM players WHERE id = (SELECT MAX(id) FROM players) ORDER BY escapeTime;")
    users = cursor.fetchone()
    connection.close()
    return users

def ranking():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()

    # Get the MAX ID (latest entry)
    cursor.execute("SELECT MAX(id) FROM players")
    latestId = cursor.fetchone()[0]

    # Find the ranking based on submission order (ID ascending)
    cursor.execute("SELECT id, name, surname FROM players ORDER BY escapeTime ASC")
    results = cursor.fetchall()
    
    connection.close()

    # Assign ranking based on ID order
    rankingDict = {user_id: rank + 1 for rank, (user_id, name,surname) in enumerate(results)}
    # Get the ranking for the latest player
    lastRank = rankingDict.get(latestId, "Unranked")
    return lastRank, ranking

def threeTopData():
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

def databaseClear():
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM players;")
        connection.commit()
        connection.close()
    

if __name__ == '__main__':
    result = checkUnique('154496M')
    print(result)