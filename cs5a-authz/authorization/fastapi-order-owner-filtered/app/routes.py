from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.db import get_db
from app.models import Order

router = APIRouter(prefix="/orders")


@router.get("/{order_id}")
def read_order(order_id: int, user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.id == order_id, Order.owner_id == user.id).first()
