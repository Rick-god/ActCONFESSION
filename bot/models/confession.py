from bot.database.connection import Base
from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column

class Confessions(Base):
    __tablename__ = "confessions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    confession_message = Column(String, nullable=False)
    confessor_id = Column(String, ForeignKey("users.unique_id"))
    status = Column(String, default="pending")
    confession_num = Column(Integer, unique=True, autoincrement=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    validator_id = Column(Integer, ForeignKey("users.id"), nullable=True)

