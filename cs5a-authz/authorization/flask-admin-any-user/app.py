from flask import Flask
from flask_login import LoginManager, login_required
from flask_wtf.csrf import CSRFProtect

from app.models import User, db

app = Flask(__name__)
LoginManager(app)
CSRFProtect(app)


@app.route("/admin/users/<int:user_id>/promote", methods=["POST"])
@login_required
def promote_user(user_id):
    db.session.query(User).filter(User.id == user_id).update({"is_admin": True})
    db.session.commit()
    return "", 204
