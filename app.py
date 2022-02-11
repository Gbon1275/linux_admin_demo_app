from flask import Flask

app = Flask(__name__)

@app.route("/")

def intro():
    return "<p>Welcome to the world of Linux Administration</p>"
