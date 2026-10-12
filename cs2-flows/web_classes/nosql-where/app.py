from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
users = MongoClient("mongodb://mongo:27017")["app"]["users"]


@app.route("/users/search")
def search():
    name = request.args["name"]
    found = users.find({"$where": "this.name == '" + name + "'"})
    return {"count": len(list(found))}
