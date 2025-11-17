from bot.database.connection import engine, Base
from bot.models.user import User
from bot.models.confession import Confession
from bot.models.comment import Comment, CommentReaction
from init_db import init_db 

try:
    init_db()
    print("Database initialized! Ready to build the bot.")
except Exception as e:
    print("Exception: ", e)

