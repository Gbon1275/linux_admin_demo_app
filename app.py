from flask import Flask

app = Flask(__name__)

@app.route("/")

def intro():
    return "<p>Your on your way to being a Linux pro</p>"