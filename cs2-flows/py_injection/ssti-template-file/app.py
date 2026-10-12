from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name", "guest")
    return render_template("hello.html", name=name)
