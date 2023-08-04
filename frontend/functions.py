from flask import Flask, render_template, request, session, redirect, url_for  

# Checks credentials from AWS
def check_credentials(username, password):
    print("checking credentials")
    return True
