import os

from flask import Flask, request

app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]


@app.route("/reports")
def reports():
    if request.cookies.get("role") == "admin":
        return {"reports": "every tenant"}
    return {"reports": "yours"}
