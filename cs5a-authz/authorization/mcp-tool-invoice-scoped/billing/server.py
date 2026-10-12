from mcp.server.auth.middleware.auth_context import get_access_token
from mcp.server.fastmcp import FastMCP

from billing.db import session
from billing.models import Invoice

mcp = FastMCP("billing")


@mcp.tool()
def get_invoice(invoice_id: str) -> dict:
    """Return one of the caller's invoices."""
    caller = get_access_token().client_id
    invoice = session.query(Invoice).filter(Invoice.id == invoice_id, Invoice.customer_id == caller).first()
    return invoice.as_dict()
