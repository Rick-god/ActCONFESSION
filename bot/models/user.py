import enum
from bot.database.connection import Base
from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column

class USERROLE(enum.Enum):
    USER = "user"
    VALIDATOR = "validator"
    ADMIN = "admin"

class USERSTATUS(enum.Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(String, default="Anonymous")
    bio = Column(String, default="Not set")
    points = Column(Integer, default=0)
    unique_id = Column(String, unique=True, index=True)
    telegram_id_hash = Column(String, unique=True, nullable=False)
    role = Column(Enum(USERROLE), default=USERROLE.USER)
    status = Column(Enum(USERSTATUS), default=USERSTATUS.ACTIVE)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

