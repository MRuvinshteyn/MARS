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

@app.route('/')
def home():
    app.secret_key = os.urandom(32)
    if session.has_key('username') == False:
        return render_template('login.html')
    else:
        session['username'] = request.args['username']
        return render_template('welcome.html', UN = session['username'])

if __name__ == '__main__':
    app.debug = True
    app.run()
