import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    domain = request.args["domain"]
    return subprocess.run(["whois", domain], capture_output=True, text=True).stdout
