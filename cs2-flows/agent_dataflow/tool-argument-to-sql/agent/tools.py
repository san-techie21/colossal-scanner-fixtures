import sqlite3

from agents import function_tool

conn = sqlite3.connect("orders.db")


@function_tool
def order_status(customer: str) -> list:
    """Look up a customer's orders."""
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, status FROM orders WHERE customer = '{customer}'")
    return cursor.fetchall()
