from flask import Flask, render_template, request, session, redirect, url_for
from flaskext.mysql import MySQL
import sys

sys.path.append("../database")
import db_functions
import functions

# TESTING DATA
subscribed_states = ["test1", "test2"]
starting_dash_state = subscribed_states[0]
recent_hearings = []
hearing = {"topic": "Test topic", "date": "00-00-0000", "length": "13:29"}
recent_hearings.append(hearing)

app = Flask(__name__)
app.secret_key = "aslfhc82173hasbcmao$&91lasf9*27129)84c"


# secret = db_functions.get_db_secret()
# db = db_functions.connect_to_db()
# app.config["MYSQL_HOST"] = secret["host"]
# app.config["MYSQL_USER"] = secret["username"]
# app.config["MYSQL_PASSWORD"] = secret["password"]
# app.config["MYSQL_DB"] = "statescribe"
# app.config["MYSQL_PORT"] = 3306
# mysql = MySQL(app)

data = { 
    "username" : "", 
    "subscribed states" : subscribed_states,
    "current state" : starting_dash_state, 
    "recent hearings" : recent_hearings 
    }


# Log in functionality
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data["username"] = request.form["username"]
        password = request.form["password"]
        valid_credentials = functions.check_credentials(data["username"], password)
        if valid_credentials:
            session["username"] = data["username"]
            return redirect(url_for("dashboard", data=data))
        else:
            return render_template(
                "pages/login.html",
                error="Invalid username or password. Please try again.",
            )
    else:
        return render_template("pages/login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/default_dashboard/")
def default_dashboard():
    return redirect(url_for("dashboard", data=data))

@app.route("/dashboard")
@app.route("/dashboard/<state>")
def dashboard(state=None):
    if state == None:
        data["current state"] = starting_dash_state

    return functions.navigate_to_page(session, "pages/portal/dashboard.html", data)

@app.route("ajdashboard")
def ajdashboard():
    with open('templates/pages/ajdashboard.html', 'r') as file:
        page_content = file.read()
    
    return page_content 


@app.route("/profile")
def profile():
    return functions.navigate_to_page(session, "pages/portal/profile.html", data)

@app.route("/basic_table")
def basic_table():
    return functions.navigate_to_page(session, "pages/portal/basic_table.html", data)

@app.route("/icon_preview")
def icon_preview():
    return functions.navigate_to_page(session, "pages/portal/fontawesome.html", data)

@app.route("/hearings")
@app.route("/hearings/<state>")
def stateinfo(state=None):
    if state == None:
        data["current state"] = starting_dash_state

    return functions.navigate_to_page(session, "pages/portal/hearing_page.html", data)

# Main Driver Function
if __name__ == "__main__":
    # Run the application on the local development server
    app.run(debug=True)
