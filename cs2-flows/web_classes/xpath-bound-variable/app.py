from lxml import etree

from flask import Flask, request

app = Flask(__name__)

TREE = etree.parse("users.xml")


@app.route("/user")
def find_user():
    name = request.args["name"]
    return {"found": len(TREE.xpath(".//user[name/text()=$name]", name=name))}
