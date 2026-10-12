from flask import Flask
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect

from app.models import Note, db

app = Flask(__name__)
LoginManager(app)
CSRFProtect(app)


@app.route("/notes/<int:note_id>/archive", methods=["POST"])
def archive_note(note_id):
    db.session.query(Note).filter(Note.id == note_id, Note.owner_id == current_user.id).update({"archived": True})
    db.session.commit()
    return "", 204
