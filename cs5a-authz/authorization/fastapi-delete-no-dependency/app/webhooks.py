from fastapi import APIRouter, Depends

from app.db import get_db
from app.models import Webhook

router = APIRouter(prefix="/webhooks")


@router.delete("/{webhook_id}")
def delete_webhook(webhook_id: int, db=Depends(get_db)):
    db.query(Webhook).filter(Webhook.id == webhook_id).delete()
    db.commit()
