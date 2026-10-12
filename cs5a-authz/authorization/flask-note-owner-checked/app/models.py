from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    body = db.Column(db.Text)
