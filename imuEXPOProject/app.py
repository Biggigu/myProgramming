from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv
import os
import mysql.connector

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database Configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", ""),
    "database": os.getenv("DB_NAME", "expo_leaderboard")
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data.get("name")
    email = data.get("email")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO participants (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()
    
    return redirect(url_for('leaderboard'))

@app.route('/leaderboard')
def leaderboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, escape_time FROM participants ORDER BY escape_time ASC LIMIT 10")
    leaders = cursor.fetchall()
    conn.close()
    
    return render_template("leaderboard.html", leaders=leaders)

@app.route('/submit_time', methods=['POST'])
def submit_time():
    data = request.get_json()
    name = data.get("name")
    escape_time = data.get("escape_time")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE participants SET escape_time = %s WHERE name = %s", (escape_time, name))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Time recorded successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
