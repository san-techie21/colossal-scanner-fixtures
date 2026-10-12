import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/preview")
def preview():
    url = request.args["url"]
    return requests.get(url, timeout=5).text
