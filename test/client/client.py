from flask import *
import requests

app = Flask(__name__)
SERVER_URL = "http://127.0.0.1:5000/follow"

@app.route("/follow")
def follow_url():
    url = request.args.get("url", "")
    if url:
        params = {
            "key": "",
            "endpoint": url
        }
        return (requests.get(SERVER_URL, params=params).text)
    
    print("No URL parameters received")
    return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("index.html")