from flask import *
import requests

app = Flask(__name__)

@app.route("/follow", methods=["GET"])
def follow_url():
    endpoint = request.args.get("endpoint", "")
    if endpoint:
        return requests.get(endpoint).text



@app.route("/admin")
def admin():
    return "Welcome to the admin page"