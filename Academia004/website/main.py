from flask import Flask, render_template, request, jsonify, redirect, session, flash
from datetime import datetime, timedelta
import databaseHandler as dbHandle
from exportDatabase import exportDB, exportData
import threading, webbrowser, os

app = Flask(__name__)
app.secret_key = 'berry_secret_key'
app.permanent_session_lifetime = timedelta(minutes=5)
app.register_blueprint(exportDB)

ADMIN_PASSWORD = "admin123"

@app.route("/")
def home():
    users = dbHandle.sixTopData()
    return render_template("index.html", users=users)

@app.route("/index")
def leaderReturn():
    return redirect("/")

@app.route("/home")
def main():
    webbrowser.open_new("http://127.0.0.1:5000/leaderboard")
    return redirect("/")

@app.route("/leaderboard")
def leaderboard():
    users = dbHandle.retrieveData()
    return render_template("leaderboard.html", users=users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            surname = request.form.get('surname')

            if not name or not surname:
                return jsonify({"success": False, "message": "❌ All fields are required."})

            dbHandle.insertData(request)
            return jsonify({"success": True, "message": "✅ Registration successful! Redirecting..."})

        except Exception as e:
            print("Registration Error:", e)
            return jsonify({"success": False, "message": "❌ Something went wrong. Please try again."})

    return render_template("register.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/timerDisplay")
def timer_display():
    return render_template("timerDisplay.html")

@app.route("/result")
def result():
    users = dbHandle.retrieveData()
    message = "Better Luck next time!"
    return render_template("result.html", users=users, message=message)

@app.route("/update-time", methods=['POST'])
def update_time():
    escapeTime = request.form.get("time")

    # Ensure it's an integer string (seconds)
    if not escapeTime or not escapeTime.isdigit():
        return "Error: Invalid time format", 400

    escapeTime = int(escapeTime)
    formattedTime = f"{escapeTime // 60:02}:{escapeTime % 60:02}"

    dbHandle.updateData(formattedTime)
    users = dbHandle.retrieveData()
    position = dbHandle.ranking()[0]
    message = "Congratulations! You successfully completed the Escape Room."

    return render_template("result.html", message=message, users=users)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    error = None
    if request.method == 'POST':
        if request.form.get('admin_pass') == ADMIN_PASSWORD:
            session.permanent = True
            session['admin'] = True
        else:
            error = "❌ Incorrect password."
    return render_template("admin.html", authorized=session.get("admin", False), error=error)

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/?refresh=1")

@app.route("/export_data")
def export_data_route():
    if not session.get("admin"):
        return redirect("/")
    flash("✅ Data exported successfully. Returning to homepage...")
    return exportData()

@app.route("/delete_data")
def delete_data():
    if not session.get("admin"):
        return redirect("/")
    dbHandle.databaseClear()
    flash("🧹 Database cleared. Returning to homepage...")
    session.pop('admin', None)
    return redirect("/admin")

@app.route("/reset")
def reset_display():
    return """
    <script>
        localStorage.setItem('displayMode', 'leaderboard');
        localStorage.removeItem('timeLeft');
        localStorage.removeItem('running');
        window.location.href = '/leaderboard';
    </script>
    """

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/home")

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
