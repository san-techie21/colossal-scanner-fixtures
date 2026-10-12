import os

from flask import Flask, abort, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
REPORTS = "/srv/reports"


@app.route("/report")
def report():
    name = secure_filename(request.args["name"])
    if not name:
        abort(400)
    with open(os.path.join(REPORTS, name)) as fh:
        return fh.read()
