from pydantic import BaseModel, Field

class AudioUpload(BaseModel):
    filename: str = Field(...)
    user_id: int

    class Config:
        orm_mode = True