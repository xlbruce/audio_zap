from flask import Flask, request

app = Flask(__name__)

@app.route("/healthcheck")
def healthcheck():
    return "App is running"

