import mysql.connector
from config import Config

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(**Config.get_db_config())
        self.cursor = self.conn.cursor(dictionary=True)

    def add_participant(self, name, email, contact):
        query = "INSERT INTO participants (name, email, contact) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, email, contact))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_escape_time(self, participant_id, escape_time):
        query = "UPDATE participants SET escape_time = %s WHERE id = %s"
        self.cursor.execute(query, (escape_time, participant_id))
        self.conn.commit()

    def get_leaderboard(self, limit=10):
        query = "SELECT name, escape_time FROM participants ORDER BY escape_time ASC LIMIT %s"
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Example Usage
# db = DatabaseManager()
# db.add_participant("John Doe", "john@example.com", "123456789")
# db.update_escape_time(1, 120)
# leaderboard = db.get_leaderboard()
# print(leaderboard)
# db.close_connection()
