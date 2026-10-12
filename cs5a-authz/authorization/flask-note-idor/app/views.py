from flask import Blueprint
from flask_login import login_required

from app.models import Note

notes = Blueprint("notes", __name__, url_prefix="/notes")


@notes.route("/<int:note_id>")
@login_required
def read_note(note_id):
    note = Note.query.get_or_404(note_id)
    return {"body": note.body}
