from flask import Flask,render_template, request
import databaseHandler as dbHandle

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
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email', '')
        phone = request.form.get('phone', '')

        dbHandle.insertData(name,surname,email,phone)
        return render_template("timer.html")
    return render_template("register.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")




if __name__ == '__main__':
    #init_db()
    app.run(debug=True)

