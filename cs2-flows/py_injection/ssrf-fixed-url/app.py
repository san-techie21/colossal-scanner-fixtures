import requests
from flask import Flask, request

app = Flask(__name__)

STATUS_URL = "https://status.example.com/api/v1/summary"


@app.route("/status")
def status():
    fmt = "json" if request.args.get("format") == "json" else "text"
    return requests.get(STATUS_URL, params={"format": fmt}, timeout=5).text
