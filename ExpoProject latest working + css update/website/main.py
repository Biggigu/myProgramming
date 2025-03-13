from flask import Flask,render_template, request,jsonify
import databaseHandler as dbHandle
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        dbHandle.insertData(request)
        return render_template("timer.html")
     
    return render_template("register.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/submit-time", methods=["POST"])
def submit_time():
    data = request.get_json()
    escape_time = data.get("escapeTime", 900)  # Default 900 seconds if missing

    try:
        
        connection = dbHandle.DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE players SET escapeTime = ? WHERE id = (SELECT MAX(id) FROM players)", (escape_time,))
        connection.commit()
        connection.close()
        print(f"Saved escape time: {escape_time} seconds")
        return jsonify({"success": True, "message": "Escape time saved!"}), 200
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return jsonify({"success": False, "message": "Database error"}), 500

if __name__ == '__main__':
    #init_db()
    app.run(debug=True)

