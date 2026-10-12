from flask import Flask, redirect, request
from flask_login import LoginManager, current_user, login_required
from flask_wtf.csrf import CSRFProtect

from app.models import Transfer, db

app = Flask(__name__)
LoginManager(app)
CSRFProtect(app)


@app.route("/transfer", methods=["POST"])
@login_required
def transfer():
    db.session.add(Transfer(sender_id=current_user.id, to=request.form["to"], amount=int(request.form["amount"])))
    db.session.commit()
    return redirect("/")
