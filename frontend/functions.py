from flask import Flask, render_template, request, session, redirect, url_for  

# Checks credentials from AWS
def check_credentials(username, password):
    print("checking credentials")
    return True

# Navigates to new pages on assumtion of logged in
def auth_navigate_to_page(session, page_to):
    if("username" in session):
        username = session["username"]
        return render_template(page_to, username=username)
    else:
        return redirect(url_for("login"))
