from fastapi import APIRouter

from app.services import users

router = APIRouter(prefix="/admin")


@router.post("/users/{user_id}/disable")
def disable_user(user_id: int):
    users.disable(user_id)
    return {"disabled": user_id}
