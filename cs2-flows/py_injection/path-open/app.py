import os

from flask import Flask, request

app = Flask(__name__)

REPORTS = "/srv/reports"


@app.route("/report")
def report():
    name = request.args["name"]
    with open(os.path.join(REPORTS, name)) as fh:
        return fh.read()
