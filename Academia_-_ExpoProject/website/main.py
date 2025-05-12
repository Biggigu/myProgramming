from flask import Flask, render_template, request, jsonify, redirect, session, flash
from datetime import timedelta
import databaseHandler as dbHandle
from exportDatabase import exportDB, exportData
import threading, webbrowser, os
import hashlib

app = Flask(__name__)
app.secret_key = 'berry_secret_key'
app.permanent_session_lifetime = timedelta(minutes=5)
app.register_blueprint(exportDB)

ADMIN_PASSWORD = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"
teamName = ""

def checkPassword(password,actualPassword):
    input = hashlib.sha256(password.encode()).hexdigest()
    return input == actualPassword

@app.route("/")
def home():
    users = dbHandle.sixTopData()
    return render_template("index.html", users=users)

@app.route("/index_en")
def index_en():
    users = dbHandle.sixTopData()
    return render_template("index_en.html", users=users)

@app.route("/index")
def leaderReturn():
    return redirect("/")

@app.route("/home")
def main():
    webbrowser.open_new("http://127.0.0.1:5000/leaderboard")
    return redirect("/")

@app.route("/startGame")
def preBooking():
    users = dbHandle.dataByID("")
    check = len(users) != 0
    return render_template("confirmBooking.html", users=users, check = check)

@app.route("/searchName", methods=['GET', 'POST'])
def searchName():
    if request.method == 'POST':
        id = request.form.get("idCard")
        id =id.upper()
        if (len(id) < 8):
            padding = "0"*(8-len(id))
            id = padding + id
        users = dbHandle.dataByID(id)
        check = len(users) != 0
        if check:
            global teamName
            teamName = users[0][3]
        return render_template("confirmBooking.html", users=users, check = check)

@app.route("/leaderboard")
def leaderboard():
    users = dbHandle.retrieveData()
    return render_template("leaderboard.html", users=users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form.get("tName")
            usernameCheck = dbHandle.checkUniqueUser(username)

            if not usernameCheck:
                return jsonify({
                    "success": False,
                    "message": "❌ Il-laqam jew isem tat-tim diġà intuża. Jekk jogħġbok agħżel ieħor."
                })

            singleGroup = request.form.get("group_type") == "single"
            looping = 1 if singleGroup else int(request.form.get("players"))

            for num in range(1, looping + 1):
                id = request.form.get(f"id{num}")
                idCheck = dbHandle.checkUnique(id)
                if not idCheck:
                    return jsonify({
                        "success": False,
                        "message": "❌ Parteċipant li diġà lagħab ma jistax jerġa’ jipparteċipa."
                    })

            for num in range(1, looping + 1):
                dbHandle.insertData(request, num)

            return jsonify({
                "success": True,
                "message": "✅ Ir-reġistrazzjoni saret b’suċċess! Redirect qed isir..."
            })

        except Exception as e:
            print("Żball fil-Formola (MT):", e)
            return jsonify({
                "success": False,
                "message": "❌ Xi ħaġa marret ħażin. Jekk jogħġbok erġa’ ipprova."
            })

    return render_template("register.html")



@app.route("/register_en", methods=['GET', 'POST'])
def register_en():
    if request.method == 'POST':
        try:
            username = request.form.get("tName")
            usernameCheck = dbHandle.checkUniqueUser(username)

            if not usernameCheck:
                return jsonify({"success": False, "message": "❌ That team name is already taken. Please choose another."})

            singleGroup = request.form.get("group_type") == "single"
            looping = 1 if singleGroup else int(request.form.get("players"))

            for num in range(1, looping + 1):
                id = request.form.get(f"id{num}")
                idCheck = dbHandle.checkUnique(id)
                if not idCheck:
                    return jsonify({"success": False, "message": "❌ A player has already participated and cannot re-enter."})

            for num in range(1, looping + 1):
                dbHandle.insertData(request, num)

            return jsonify({"success": True, "message": "✅ Registration successful! Redirecting..."})

        except Exception as e:
            print("Registration Error (EN):", e)
            return jsonify({"success": False, "message": "❌ Something went wrong. Please try again."})

    return render_template("register_en.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/timerDisplay")
def timer_display():
    return render_template("timerDisplay.html")

@app.route("/result")
def result():
    users = dbHandle.retrieveData()
    message = "Congratulation for your efforts"
    return render_template("result.html", users=users, message=message)

@app.route("/update-time", methods=['GET', 'POST'])
def update_time():
    try:
        escapeTime = request.form.get("time")
        escapeTime = int(escapeTime)
    except:
        escapeTime = 0  # Default to 0 if missing or invalid

    escapeTime = int(escapeTime)
    timeTaken = 900 - escapeTime
    # Convert seconds to MM:SS format
    minutes = timeTaken // 60
    seconds = timeTaken % 60
    formattedTime = f"{minutes:02}:{seconds:02}"

    dbHandle.updateData(formattedTime, teamName)
    #users = dbHandle.retrieveData()
    #position = dbHandle.ranking()[0]
    #message = "Congratulations! You successfully completed the Escape Room."

    return redirect("index")
    #return render_template("result.html", message=message, users=users)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    users = dbHandle.retrieveData()
    error = None
    if request.method == 'POST':
        passCheck = checkPassword(request.form.get('admin_pass'),ADMIN_PASSWORD)
        if passCheck:
            session.permanent = True
            session['admin'] = True
        else:
            error = "❌ Incorrect password."
    return render_template("admin.html", authorized=session.get("admin", False), error=error,users=users)

@app.route('/deleteUser/<userID>', methods=['DELETE'])
def delete_user(userID):
    dbHandle.deleteUser(userID)
    users = dbHandle.retrieveData()
    return render_template("admin.html", authorized=session.get("admin", False),users=users)


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
