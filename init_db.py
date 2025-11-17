from bot.database.connection import engine, Base
from bot.models.user import User
from bot.models.confession import Confessions
from bot.models.comment import Comment, CommentReaction

def init_db():
    Base.metadata.create_all(bind=engine)
