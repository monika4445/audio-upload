import shutil
from pathlib import Path
from app.models.audio import Audio
from sqlalchemy.ext.asyncio import AsyncSession

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


async def upload_audio(file, user_id: int, db: AsyncSession):
    filepath = UPLOAD_DIR / file.filename
    with filepath.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_audio = Audio(filename=file.filename, filepath=str(filepath), user_id=user_id)
    db.add(new_audio)
    await db.commit()
    return new_audio


async def get_all_audio(db: AsyncSession):
    result = await db.execute(select(Audio))
    audios = result.scalars().all()
    return audios
