import re
from pydantic import BaseModel, Field, field_validator, EmailStr
from fastapi import HTTPException, status

class CreateUser(BaseModel):
    email: EmailStr
    token: str = Field(...)

    class Class:
        orm_mode = True

    @field_validator('email', mode='before')
    @classmethod
    def validate_email(cls, email: str) -> str:
        email = email.strip().lower()
        if not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email can't be empty.")

        pattern = (r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
                   r"@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+"
                   r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")

        if not re.match(pattern, email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format.")

        return email
