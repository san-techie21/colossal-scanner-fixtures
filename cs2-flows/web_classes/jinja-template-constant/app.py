from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)


@app.route("/greeting")
def greeting():
    return Template("Hello {{ name }}").render(name=request.args["name"])
