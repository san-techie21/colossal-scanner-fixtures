import pickle

from flask import Flask, request

app = Flask(__name__)


@app.route("/session", methods=["POST"])
def restore_session():
    state = pickle.loads(request.data)
    return {"user": state.get("user")}
