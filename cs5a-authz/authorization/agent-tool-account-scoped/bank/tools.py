from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool

from bank.db import accounts


@tool
def account_balance(config: RunnableConfig) -> str:
    """Return the balance of the signed-in customer's account."""
    customer = config["configurable"]["customer_id"]
    return str(accounts.find_one({"owner": customer})["balance"])
