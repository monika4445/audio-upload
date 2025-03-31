from sqlalchemy import Column, String, Integer, ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship

class Audio(Base):
    __tablename__ = "audios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="audios")