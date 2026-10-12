import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/users")
def find_user():
    name = request.args.get("name", "")
    cursor = sqlite3.connect("app.db").cursor()
    cursor.execute("SELECT id, email FROM users WHERE name = ?", (name,))
    return {"rows": cursor.fetchall()}
