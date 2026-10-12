from urllib.parse import urlparse

from flask import Flask, redirect, request

app = Flask(__name__)


@app.route("/login/done")
def login_done():
    target = request.args.get("next", "/")
    if urlparse(target).netloc not in ("", "app.example.com"):
        target = "/"
    return redirect(target)
