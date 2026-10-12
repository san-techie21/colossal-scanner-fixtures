from mcp.server.fastmcp import FastMCP

from billing.store import refund_payment

mcp = FastMCP("billing")


@mcp.tool()
def issue_refund(payment_id: str, amount_cents: int) -> str:
    """Refund part of a payment."""
    refund_payment(payment_id, amount_cents)
    return "refunded"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
