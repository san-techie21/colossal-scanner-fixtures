import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "ok"


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
