
# from flask import Flask, render_template, request, redirect, url_for, session
# app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return render_template('home.html')

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=8080)







# from flask import Flask, render_template, request, redirect, url_for, session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Required for session management

# # Home route
# @app.route("/")
# def home():
#     return render_template('home.html')

# # Login route
# @app.route("/login", methods=["POST"])
# def login():
#     # Simulating login validation (replace with real validation logic)
#     username = request.form.get("username")
#     password = request.form.get("password")
#     if username == "test" and password == "password":  # Example credentials
#         session["user"] = username  # Store user info in session
#         return redirect(url_for("dashboard"))
#     else:
#         return "Invalid credentials! Please try again."

# # Dashboard route
# @app.route("/dashboard")
# def dashboard():
#     if "user" in session:  # Check if the user is logged in
#         return render_template("dashboard.html")
#     return redirect(url_for("home"))

# # My Calendar route
# @app.route("/my-calendar")
# def my_calendar():
#     if "user" in session:  # Check if the user is logged in
#         return render_template("my-calendar.html")
#     return redirect(url_for("home"))

# # Shared Calendar route
# @app.route("/shared-calendar")
# def shared_calendar():
#     if "user" in session:  # Check if the user is logged in
#         return render_template("shared-calendar.html")
#     return redirect(url_for("home"))

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, debug=True)





# from flask import Flask, render_template, request, redirect, url_for, session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# @app.route("/")
# def home():
#     return render_template('home.html')

# @app.route("/login", methods=["POST"])
# def login():
#     username = request.form.get("username")
#     password = request.form.get("password")
#     if username == "test" and password == "password":  # Replace with real validation
#         session["user"] = username
#         return redirect(url_for("dashboard"))
#     else:
#         return "Invalid credentials! Please try again."

# @app.route("/dashboard")
# def dashboard():
#     if "user" in session:
#         return render_template("dashboard.html")
#     return redirect(url_for("home"))

# @app.route("/my-calendar")
# def my_calendar():
#     if "user" in session:
#         return render_template("my-calendar.html")
#     return redirect(url_for("home"))

# @app.route("/month/<month>")
# def month_view(month):
#     if "user" in session:
#         # Retrieve events for the specific month
#         # This is dummy data. Replace with your database logic.
#         events = [
#             {"date": "2024-01-05", "title": "New Year Celebration"},
#             {"date": "2024-01-15", "title": "Team Meeting"},
#         ]
#         events.sort(key=lambda x: x["date"])  # Sort events by date
#         return render_template("month-view.html", month=month, events=events)
#     return redirect(url_for("home"))

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, debug=True)










from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory storage for events (replace with a database in production)
events_db = {
    "January": [
        {"date": "2024-01-05", "title": "New Year Celebration"},
        {"date": "2024-01-15", "title": "Team Meeting"},
    ],
    "February": [],
    "March": [],
    # Add other months as needed
}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "test" and password == "password":  # Replace with real validation
        session["user"] = username
        return redirect(url_for("dashboard"))
    else:
        return "Invalid credentials! Please try again."

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html")
    return redirect(url_for("home"))

@app.route("/my-calendar")
def my_calendar():
    if "user" in session:
        return render_template("my-calendar.html")
    return redirect(url_for("home"))

@app.route("/month/<month>", methods=["GET", "POST"])
def month_view(month):
    if "user" not in session:
        return redirect(url_for("home"))

    if month not in events_db:
        return "Invalid month!", 404

    if request.method == "POST":
        # Add a new event
        event_date = request.form.get("date")
        event_title = request.form.get("title")
        if event_date and event_title:
            events_db[month].append({"date": event_date, "title": event_title})
            events_db[month].sort(key=lambda x: x["date"])  # Sort events by date

    # Get events for the selected month
    events = events_db.get(month, [])
    return render_template("month-view.html", month=month, events=events)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
