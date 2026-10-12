from defusedxml import ElementTree
from flask import Flask, request

app = Flask(__name__)


@app.route("/import", methods=["POST"])
def import_xml():
    doc = ElementTree.fromstring(request.data)
    return {"items": len(doc)}
