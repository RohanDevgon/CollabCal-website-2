
# from flask import Flask, render_template, request, redirect, url_for, session
# app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return render_template('home.html')

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=8080)
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Home route
@app.route("/")
def home():
    return render_template('home.html')

# Login route
@app.route("/login", methods=["POST"])
def login():
    # Simulating login validation (replace with real validation logic)
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "test" and password == "password":  # Example credentials
        session["user"] = username  # Store user info in session
        return redirect(url_for("dashboard"))
    else:
        return "Invalid credentials! Please try again."

# Dashboard route
@app.route("/dashboard")
def dashboard():
    if "user" in session:  # Check if the user is logged in
        return render_template("dashboard.html")
    return redirect(url_for("home"))

# My Calendar route
@app.route("/my-calendar")
def my_calendar():
    if "user" in session:  # Check if the user is logged in
        return render_template("my-calendar.html")
    return redirect(url_for("home"))

# Shared Calendar route
@app.route("/shared-calendar")
def shared_calendar():
    if "user" in session:  # Check if the user is logged in
        return render_template("shared-calendar.html")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
