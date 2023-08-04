from flask import Flask, render_template, request, session, redirect, url_for  
from functions import check_credentials

# TESTING DATA
subscribed_states = ["test1", "test2"]
starting_dash_state = subscribed_states[0]
recent_hearings = []
hearing = {
    "topic": "Test topic",
    "date": "00-00-0000",
    "length": "13:29"
}
recent_hearings.append(hearing)

data = {
    "starting_dash_state": starting_dash_state,
    "recent_hearings": recent_hearings,
    "subscribed_states": subscribed_states
}


app = Flask(__name__)
app.secret_key = "aslfhc82173hasbcmao$&91lasf9*27129)84c"

# Log in functionality
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        valid_credentials = check_credentials(username, password)
        if valid_credentials:
            session["username"] = username
            return redirect(url_for("dashboard", state=starting_dash_state))
        else:
            return render_template("pages/login.html", error="Invalid username or password. Please try again.")
    else:
        return render_template("pages/login.html")
    
@app.route('/logout')  
def logout():  
    session.pop('username', None)  
    return redirect(url_for('login'))  

@app.route("/default_dashboard/")
def default_dashboard():
    return redirect(url_for("dashboard", state=starting_dash_state))

@app.route("/dashboard")
@app.route("/dashboard/<state>")
def dashboard(state=None):
    if("username" not in session):
        return redirect(url_for("login"))
    username = session["username"]

    if(state == None):
        state = starting_dash_state

    return render_template("pages/portal/dashboard.html", username=username, state=state, data=data)

        

@app.route("/profile")
def profile():
    if("username" not in session):
        return redirect(url_for("login"))
    username = session["username"]
    return render_template("pages/portal/profile.html", username=username)

@app.route("/basic_table")
def basic_table():
    if("username" not in session):
        return redirect(url_for("login"))
    username = session["username"]
    return render_template("pages/portal/basic_table.html", username=username)

@app.route("/icon_preview")
def icon_preview():
    if("username" not in session):
        return redirect(url_for("login"))
    username = session["username"]
    return render_template("pages/portal/fontawesome.html", username=username)


# Main Driver Function
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)
