import ast

from flask import Flask, request

app = Flask(__name__)


@app.route("/calc")
def calc():
    expression = request.args["expr"]
    return str(ast.literal_eval(expression))
