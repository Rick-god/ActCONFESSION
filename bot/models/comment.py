from bot.database.connection import Base
from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from bot.models.user import User
from bot.models.confession import Confessions

class Comment(Base):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comment_content = Column(Text, nullable=False)
    media_type = Column(String, nullable=True)
    media_file_id = Column(String, nullable=True)
    
    confession_id = Column(Integer, ForeignKey("confessions.id"), nullable=False)
    commenter_id = Column(String, ForeignKey("users.unique_id"))
    
    main_comment_id = Column(Integer, ForeignKey("comments.id"), nullable=True)
    likes_count = Column(Integer, default=0, nullable=False)
    dislikes_count = Column(Integer, default=0, nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    confession = relationship("Confession", back_populates="comments")
    commenter = relationship("User", back_populates="comments")
    replies = relationship("Comment", back_populates="main_comment")
    main_comment = relationship("Comment", remote_side=[id], back_populates="replies")
    
class CommentReaction(Base):
    __tablename__ = "comment_reactions"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comment_id = Column(Integer, ForeignKey("comments.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.unique_id"), nullable=False)
    reaction_type = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (UniqueConstraint('comment_id', 'user_id', name='unique_user_reaction'),)