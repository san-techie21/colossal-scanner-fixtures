from flask import make_response

from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    response = make_response({"ok": True})
    response.set_cookie("session", issue_session(request.form["user"]), secure=True, httponly=True, samesite="Lax")
    return response
