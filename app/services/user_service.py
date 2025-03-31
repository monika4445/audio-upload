from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def get_user_by_email(email: str, db: AsyncSession):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

async def create_user(email: str, token: str, db: AsyncSession):
    new_user = User(email=email, token=token)
    db.add(new_user)
    await db.commit()
    return new_user
