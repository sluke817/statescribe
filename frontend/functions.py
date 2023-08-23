# Checks credentials from AWS
from flask import Flask, render_template, request, session, redirect, url_for
from flaskext.mysql import MySQL

def check_credentials(username, password):
    print("checking credentials")
    return True

def navigate_to_page(session, page, data):
    if "username" not in session:
        return redirect(url_for("login"))
    data["username"] = session["username"]
    return render_template(page, data=data)
