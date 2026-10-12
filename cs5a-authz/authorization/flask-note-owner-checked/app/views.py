from flask import Blueprint, abort
from flask_login import current_user, login_required

from app.models import Note

notes = Blueprint("notes", __name__, url_prefix="/notes")


@notes.route("/<int:note_id>")
@login_required
def read_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.owner_id != current_user.id:
        abort(403)
    return {"body": note.body}
