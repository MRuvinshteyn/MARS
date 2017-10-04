#!/usr/bin/python

"""
Michael Ruvinshteyn && Anish Shenoy
SoftDev1 pd7
HW07 -- Do I Know You?
2017 - 10 - 4
"""

from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route('/')
def home():
    if session.has_key('username') == True: #renders welcome page if a 'username' key exists
        return render_template('welcome.html',UN = session['username'])
    return render_template('login.html') #otherwise renders the login page

@app.route('/login', methods=['POST']) #uses POST method for form submission
def login():
    if request.form['username'] == 'admin': #the only correct username is "admin"
        if request.form['password'] == 'password': #the only correct password is "password"
            session['username'] = 'admin' #sets the 'username' key to something so that it can be recognized
            return render_template('login_success.html') #tells the user they are logged in
    return render_template('login_fail.html') #otherwise tells the user their credentials were incorrect

@app.route('/logout')
def logout():
    session.clear() #clears the session to remove the 'username' key
    return redirect(url_for('home')) #redirects user back to homepage

if __name__ == '__main__':
    app.debug = True
    app.run()
