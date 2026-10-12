import os

from flask import Flask, request

app = Flask(__name__)

FILES = "/srv/files"


@app.route("/files/<path:name>", methods=["DELETE"])
def delete(name):
    os.remove(os.path.join(FILES, name))
    return {"ok": True}
