from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp import FastMCP

from billing.auth import IntrospectionVerifier
from billing.store import refund_payment

mcp = FastMCP(
    "billing",
    token_verifier=IntrospectionVerifier(),
    auth=AuthSettings(issuer_url="https://idp.example.com", resource_server_url="https://billing.example.com",
                      required_scopes=["billing:refund"]),
)


@mcp.tool()
def issue_refund(payment_id: str, amount_cents: int) -> str:
    """Refund part of a payment."""
    refund_payment(payment_id, amount_cents)
    return "refunded"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
