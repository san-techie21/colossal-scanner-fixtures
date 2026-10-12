from flask import Flask
from flask_login import login_required

from app.models import Invoice

app = Flask(__name__)


@app.route("/invoices/<int:invoice_id>")
@login_required
def show_invoice(invoice_id):
    invoice = Invoice.query.filter_by(id=invoice_id).first_or_404()
    return invoice.to_dict()
