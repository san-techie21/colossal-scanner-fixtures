from flask import Flask, request
from flask_login import current_user, login_required

from app.models import db

app = Flask(__name__)
EDITABLE = {"display_name", "timezone"}


@app.route("/profile", methods=["PUT"])
@login_required
def update_profile():
    for field, value in request.get_json().items():
        if field in EDITABLE:
            setattr(current_user, field, value)
    db.session.commit()
    return {"ok": True}
