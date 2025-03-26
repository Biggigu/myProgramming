from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Home Page with Leaderboard
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Get top 3 fastest escape times
    cursor.execute("SELECT name, escape_time FROM participants ORDER BY escape_time ASC LIMIT 3")
    leaderboard = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('index.html', leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
