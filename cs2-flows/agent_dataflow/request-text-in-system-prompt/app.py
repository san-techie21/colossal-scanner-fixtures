import anthropic
from flask import Flask, request

app = Flask(__name__)
client = anthropic.Anthropic()


@app.route("/support", methods=["POST"])
def support():
    note = request.json["customer_note"]
    system = "You are the refunds assistant. Follow the refund policy. Customer note: " + note
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=400,
        system=system,
        messages=[{"role": "user", "content": "Decide the refund."}],
    )
    return {"answer": reply.content[0].text}
