from fastapi import APIRouter, Depends

from app.auth import User, require_admin
from app.services import users

router = APIRouter(prefix="/admin")


@router.post("/users/{user_id}/disable")
def disable_user(user_id: int, admin: User = Depends(require_admin)):
    users.disable(user_id)
    return {"disabled": user_id}
