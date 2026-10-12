from flask import Flask, request
from lxml import etree

app = Flask(__name__)
PARSER = etree.XMLParser(resolve_entities=True, no_network=False)


@app.route("/import", methods=["POST"])
def import_xml():
    doc = etree.fromstring(request.data, PARSER)
    return {"items": len(doc)}
