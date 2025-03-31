from fastapi import APIRouter, UploadFile, File, Depends
from app.services.audio_service import upload_audio, get_all_audio
from app.databases.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/audio", tags=["Audio"])

@router.post("/upload/")
async def upload_audio_route(file: UploadFile = File(...), user_id: int = 1, db: AsyncSession = Depends(get_db)):
    new_audio = await upload_audio(file, user_id, db)
    return {"filename": new_audio.filename, "filepath": new_audio.filepath}

@router.get("/list/")
async def list_audio(db: AsyncSession = Depends(get_db)):
    audios = await get_all_audio(db)
    return audios
