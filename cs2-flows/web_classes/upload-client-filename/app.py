import os

from flask import Flask, request

app = Flask(__name__)

UPLOADS = "/srv/uploads"


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join(UPLOADS, file.filename))
    return {"ok": True}
