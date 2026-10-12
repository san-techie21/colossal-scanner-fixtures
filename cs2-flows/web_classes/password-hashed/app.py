from flask import Flask, request

app = Flask(__name__)

from werkzeug.security import generate_password_hash

from app.models import User, db


@app.route("/register", methods=["POST"])
def register():
    user = User(username=request.form["username"],
                password=generate_password_hash(request.form["password"]))
    db.session.add(user)
    db.session.commit()
    return {"ok": True}
