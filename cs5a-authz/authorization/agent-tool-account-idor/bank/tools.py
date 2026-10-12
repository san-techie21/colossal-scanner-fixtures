from langchain_core.tools import tool

from bank.db import accounts


@tool
def account_balance(account_id: str) -> str:
    """Return the balance of an account."""
    return str(accounts.find_one({"_id": account_id})["balance"])
