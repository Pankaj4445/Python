from flask import flask_frame
app=Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Welcome</h1>"+10
@app.route("/user")
def user():
    return "<h1><b>Welcome to webpage</b></h1>"
