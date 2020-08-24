from flask import Flask, render_template, url_for, redirect
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return redirect(url_for('login'))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/user')
def user():
    return jsonify(
        username="Coke",
        title="Boss",
        comment="do not give me such a task again"
    )
