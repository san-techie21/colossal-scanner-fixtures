import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/session", methods=["POST"])
def restore_session():
    state = json.loads(request.data)
    return {"user": state.get("user")}
