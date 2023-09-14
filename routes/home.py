from flask import Blueprint
from flask import render_template

home = Blueprint('dashboard', __name__)

@home.route('/')
def dashboard():
    return render_template('index.html')