from mcp.server.fastmcp import FastMCP

from billing.db import session
from billing.models import Invoice

mcp = FastMCP("billing")


@mcp.tool()
def get_invoice(invoice_id: str) -> dict:
    """Return one invoice."""
    invoice = session.get(Invoice, invoice_id)
    return invoice.as_dict()
