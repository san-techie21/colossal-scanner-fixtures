from flask import Flask

from app.models import Project, db

app = Flask(__name__)


@app.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    project = db.session.get(Project, project_id)
    db.session.delete(project)
    db.session.commit()
    return "", 204
