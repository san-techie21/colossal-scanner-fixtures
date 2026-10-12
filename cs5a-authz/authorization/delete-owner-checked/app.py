from flask import Flask, abort
from flask_login import current_user, login_required

from app.models import Project, db

app = Flask(__name__)


@app.route("/projects/<int:project_id>", methods=["DELETE"])
@login_required
def delete_project(project_id):
    project = db.session.get(Project, project_id)
    if project is None or project.owner_id != current_user.id:
        abort(404)
    db.session.delete(project)
    db.session.commit()
    return "", 204
