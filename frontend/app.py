from flask import Flask, render_template, request, session, redirect, url_for  
from functions import check_credentials, auth_navigate_to_page


app = Flask(__name__)
app.secret_key = "aslfhc82173hasbcmao$&91lasf9*27129)84c"

# Log in functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        valid_credentials = check_credentials(username, password)
        if valid_credentials:
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("pages/login.html", error="Invalid username or password. Please try again.")
    else:
        return render_template("pages/login.html")
    
@app.route('/logout')  
def logout():  
    session.pop('username', None)  
    return redirect(url_for('login'))  

@app.route("/dashboard")
def dashboard():
    return auth_navigate_to_page(session, "pages/portal/dashboard.html")

@app.route("/profile")
def profile():
    return auth_navigate_to_page(session, "pages/portal/profile.html")

@app.route("/basic_table")
def basic_table():
    return auth_navigate_to_page(session, "pages/portal/basic-table.html")
