import sqlite3
from flask import jsonify,request

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
        cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50),
                        surname VARCHAR(50),
                        username VARCHAR(50),
                        email VARCHAR(50),
                        phone VARCHAR(50),
                        team BOOLEAN,
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
    """ connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('UPDATE players SET escapeTime = ? WHERE id = (SELECT MAX(id) FROM players);',
                   (escapeTime,))
    connection.commit()
    connection.close() """

    return jsonify({'message': 'Code need to be adjusted accordingly'})

def retrieveData():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT name || ' ' || surname AS 'username', email, phone, escapeTime FROM players ORDER BY escapeTime;")
    users = cursor.fetchall()
    connection.close()
    return users

# For sending emails
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

def sixTopData():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute("SELECT name || ' ' || surname AS 'username', escapeTime FROM players ORDER BY escapeTime LIMIT 6;")
    users = cursor.fetchall()
    connection.close()
    return users


def deleteUser(value):
        try:
            connection = DatabaseConnection().connect()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM players WHERE id = ?", (value,))
            connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
        finally:
            connection.close()

def databaseClear():
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM players;")
        # Reset the autoincrementing ID
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='players';")
        connection.commit()
        connection.close()
        
if __name__ == '__main__':
    DatabaseConnection.newDBIfNoExist()