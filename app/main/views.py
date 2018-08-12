from flask import render_template
from . import main

@main.route('/login')
def login():
    return render_template('main/login.html')

