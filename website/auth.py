from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    return render_template("appartayou.html")
    #return "<h1> Test</h1>"
