from flask import Flask, abort
from flask_login import LoginManager, current_user, login_required
from flask_wtf.csrf import CSRFProtect

from app.models import User, db

app = Flask(__name__)
LoginManager(app)
CSRFProtect(app)


@app.route("/admin/users/<int:user_id>/promote", methods=["POST"])
@login_required
def promote_user(user_id):
    if not current_user.is_admin:
        abort(403)
    db.session.query(User).filter(User.id == user_id).update({"is_admin": True})
    db.session.commit()
    return "", 204
