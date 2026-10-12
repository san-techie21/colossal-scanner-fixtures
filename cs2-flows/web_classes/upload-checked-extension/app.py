import os

from werkzeug.utils import secure_filename

from flask import Flask, request

app = Flask(__name__)

UPLOADS = "/srv/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg"}


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    name = secure_filename(file.filename)
    if name.rsplit(".", 1)[-1].lower() not in ALLOWED_EXTENSIONS:
        return {"error": "type not allowed"}, 400
    file.save(os.path.join(UPLOADS, name))
    return {"ok": True}
