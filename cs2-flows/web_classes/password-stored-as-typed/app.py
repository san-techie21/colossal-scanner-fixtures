from flask import Flask, request

app = Flask(__name__)

from app.models import User, db


@app.route("/register", methods=["POST"])
def register():
    user = User(username=request.form["username"],
                password=request.form["password"])
    db.session.add(user)
    db.session.commit()
    return {"ok": True}
