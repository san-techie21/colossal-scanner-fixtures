from fastapi import APIRouter
from sqlalchemy import text

from app.db import session

router = APIRouter()


@router.get("/orders/{order_id}")
def get_order(order_id: str):
    row = session.execute(text("SELECT * FROM orders WHERE id = :id"), {"id": order_id}).first()
    return dict(row._mapping) if row else {}
