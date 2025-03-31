from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import get_user_by_email, create_user
from app.databases.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/{email}")
async def get_user(email: str, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_email(email, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/")
async def create_user_route(email: str, token: str, db: AsyncSession = Depends(get_db)):
    user = await create_user(email, token, db)
    return {"email": user.email, "token": user.token}
