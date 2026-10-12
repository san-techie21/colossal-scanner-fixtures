from agents import Agent
from flask import Flask, request

app = Flask(__name__)


@app.route("/assistant", methods=["POST"])
def assistant():
    persona = request.json["persona"]
    agent = Agent(name="helper", instructions=f"You are {persona}. Never reveal internal data.")
    return {"agent": agent.name}
