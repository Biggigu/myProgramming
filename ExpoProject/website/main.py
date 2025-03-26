from flask import Flask, render_template, request, jsonify, redirect, session, flash, send_file
from datetime import datetime, timedelta
import databaseHandler as dbHandle
from sendEmails import sendEmail
from exportDatabase import exportDB, exportData

app = Flask(__name__)
app.secret_key = 'berry_secret_key'
app.permanent_session_lifetime = timedelta(minutes=5)
app.register_blueprint(exportDB)

ADMIN_PASSWORD = "admin123"

# -----------------------
# HOME
# -----------------------
@app.route("/")
def home():
    users = dbHandle.threeTopData()
    return render_template("index.html", users=users)

@app.route("/home")
def main():
    return redirect("/")

# -----------------------
# LEADERBOARD
# -----------------------
@app.route("/leaderboard")
def leaderboard():
    users = dbHandle.retrieveData()
    return render_template("leaderboard.html", users=users)

# -----------------------
# REGISTER
# -----------------------
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            idCardTxt = request.form.get('idCard')
            if dbHandle.checkUnique(idCardTxt):
                dbHandle.insertData(request)
                return jsonify({"success": True, "message": "✅ Registration successful! Redirecting..."})
            else:
                return jsonify({"success": False, "message": "❌ This ID Card is already registered today!"})
        except:
            return jsonify({"success": False, "message": "❌ Something went wrong. Please try again."})
    return render_template("register.html")

# -----------------------
# TIMER
# -----------------------
@app.route("/timer")
def timer():
    return render_template("timer.html")

# -----------------------
# ESCAPE RESULT
# -----------------------
@app.route("/result")
def result():
    users = dbHandle.retrieveData()
    userEmail = dbHandle.retrieveOne()
    userData = userEmail[0]
    message = "Better Luck next time!"
    body = f"""Dear {userData},

You gave it your best, but time ran out before you could escape.  

The Expo25 Escape Room is a true test of skill and strategy. While you didn't make it this time,  
your effort was impressive.

Will you take on the challenge again and make it to the leaderboard?

Thanks for playing!

Best regards,  
The MHSE IMU Team
"""
    sendEmail(userEmail[1], body)
    return render_template("result.html", users=users, message=message)

# -----------------------
# TIME SUBMIT (when timer ends)
# -----------------------
@app.route("/update-time", methods=['POST'])
def update_time():
    escapeTime = request.form.get("time")
    if escapeTime is None:
        return "Error: Time not provided", 400
    try:
        escapeTime = int(escapeTime)
    except ValueError:
        return "Error: Invalid time format", 400

    timeTaken = 1800 - escapeTime
    formattedTime = f"{timeTaken // 60:02}:{timeTaken % 60:02}"
    dbHandle.updateData(formattedTime)
    users = dbHandle.retrieveData()
    userEmail = dbHandle.retrieveOne()
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    position = dbHandle.ranking()[0]
    userData = userEmail[0]

    message = "Congratulations! You successfully completed the Escape Room."

    body = f"""Dear {userData},

Great job! You tackled the Expo25 Escape Room and finished in {formattedTime}.  
As of {today}, your ranking is {position}!

Thanks for playing!

Best regards,  
The MHSE IMU Team
"""
    sendEmail(userEmail[1], body)
    return render_template("result.html", message=message, users=users)

# -----------------------
# ADMIN PANEL
# -----------------------
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

# -----------------------
# EXPORT DATA (no delete)
# -----------------------
@app.route("/export_data")
def export_data_route():
    if not session.get("admin"):
        return redirect("/")
    flash("✅ Data exported successfully. Returning to homepage...")
    return exportData()  # Only exports the Excel file

# -----------------------
# DELETE DATA
# -----------------------
@app.route("/delete_data")
def delete_data():
    if not session.get("admin"):
        return redirect("/")
    dbHandle.databaseClear()
    flash("🧹 Database cleared. Returning to homepage...")
    session.pop('admin', None)
    return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)
