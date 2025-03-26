from flask import Flask, render_template, request, jsonify
import databaseHandler as dbHandle
from sendEmails import sendEmail
from datetime import datetime
from exportDatabase import exportDB

app = Flask(__name__)
app.register_blueprint(exportDB)

@app.route("/")
def home():
    users = dbHandle.threeTopData()
    return render_template("index.html", users=users)

@app.route("/home")
def main():
    users = dbHandle.threeTopData()
    return render_template("index.html", users=users)

@app.route("/leaderboard")
def leaderboard():
    users = dbHandle.retrieveData()
    return render_template("leaderboard.html", users=users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            idCardTxt = request.form.get('idCard')
        
            if (dbHandle.checkUnique(idCardTxt)):
                dbHandle.insertData(request)
                return jsonify({"success": True, "message": "✅ Registration successful! Redirecting..."})
            else:
                return jsonify({"success": False, "message": "❌ This ID Card is already registered today!"})
    
        except Exception as e:
            return jsonify({"success": False, "message": "❌ Something went wrong. Please try again."})

    return render_template("register.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/result")
def result():
    users = dbHandle.retrieveData()
    userEmail = dbHandle.retrieveOne()
    userData = userEmail[0]
    userEmail = dbHandle.retrieveOne()
    message = "Better Luck next time!"
    body = f"""Dear {userData},

    You gave it your best, but time ran out before you could escape.  

    The Expo25 Escape Room is a true test of skill and strategy. While you didn't make it this time,  
    your effort was impressive. Many have tried, and only a few succeed.  

    Will you take on the challenge again and make it to the leaderboard?  

    Thanks for playing—we hope you had an amazing time!  

    Best regards,  
    The MHSE IMU Team
    """
    messageEmail = f"""{body}"""
    messageEmail = messageEmail
    sendEmail(userEmail[1],messageEmail)
    return render_template("result.html", users=users, message=message)

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
    print(timeTaken)
    print(timeTaken)
    # Convert seconds to MM:SS format
    minutes = timeTaken // 60
    seconds = timeTaken % 60
    formattedTime = f"{minutes:02}:{seconds:02}"
    
    message = "Congratulations! You successfully completed the Escape Room."
    dbHandle.updateData(formattedTime)
    users = dbHandle.retrieveData()
    userEmail = dbHandle.retrieveOne()

    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    position = dbHandle.ranking()[0]
    userData = userEmail[0]

    body = f"""Dear {userData},  

    Great job! You tackled the Expo25 Escape Room and finished in {formattedTime}.  
    As of {today}, your ranking is {position}!

    But the big question is… can anyone beat your time before the day ends?

    Keep an eye on the leaderboard and see if you stay on top!  

    Thanks for playing, we hope you had an amazing time!  

    Best regards,  
    The MHSE IMU Team
    """
    messageEmail = f"""{body}"""
  
    messageEmail = messageEmail
    sendEmail(userEmail[1],messageEmail)
    return render_template("result.html", message=message, users=users)

if __name__ == '__main__':
    app.run(debug=True)
