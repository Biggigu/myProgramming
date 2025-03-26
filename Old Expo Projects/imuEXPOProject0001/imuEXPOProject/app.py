from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    """Initialize the database."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        surname TEXT,
                        email TEXT,
                        phone TEXT,
                        escape_time TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email', '')
        phone = request.form.get('phone', '')
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players (name, surname, email, phone) VALUES (?, ?, ?, ?)',
                       (name, surname, email, phone))
        conn.commit()
        conn.close()
        
        return render_template('timer.html')
    return render_template('register.html')

@app.route('/leaderboard-data')
def leaderboard_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name || " " || surname, escape_time FROM players ORDER BY escape_time ASC LIMIT 10')
    data = [{'username': row[0], 'time': row[1]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

@app.route('/submit-time', methods=['POST'])
def submit_time():
    name = request.form.get('name')
    surname = request.form.get('surname')
    escape_time = request.form.get('escape_time')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE players SET escape_time = ? WHERE name = ? AND surname = ?',
                   (escape_time, name, surname))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Time recorded successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
