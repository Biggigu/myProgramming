from flask import Flask, redirect,render_template, request, jsonify, url_for
import databaseHandler as dbHandle

app = Flask(__name__)

@app.route("/")
def home():
    users = dbHandle.ThreeTopData()
    return render_template("index.html", users=users)

@app.route("/home")
def main():
    users = dbHandle.ThreeTopData()
    return render_template("index.html", users=users)

@app.route("/leaderboard")
def leaderboard():
    users = dbHandle.retrieveData()
    return render_template("leaderboard.html", users=users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        dbHandle.insertData(request)
        return redirect(url_for("timer"))
     
    return render_template("register.html")

@app.route("/result")
def result():
    users = dbHandle.retrieveData()
    return render_template("result.html", users=users)

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/update-time", methods=['POST'])
def update_time():
    escapeTime = request.form.get("time")
    
    # Handle missing or invalid time input
    if escapeTime is None:
        return "Error: Time not provided", 400  # Or handle it as appropriate

    try:
        escapeTime = int(escapeTime)
    except ValueError:
        return "Error: Invalid time format", 400  # Handle invalid integer input

    timeTaken = 900 - escapeTime
    print(timeTaken)
    print(timeTaken)
    # Convert seconds to MM:SS format
    minutes = timeTaken // 60
    seconds = timeTaken % 60
    formattedTime = f"{minutes:02}:{seconds:02}"
    
    # Assuming you have a function in databaseHandler to update the time taken
    dbHandle.updateData(formattedTime)
        
    return redirect(url_for("result"))

if __name__ == '__main__':
    #init_db()
    app.run(debug=True)

