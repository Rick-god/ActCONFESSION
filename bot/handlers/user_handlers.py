from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from bot.database.connection import get_db
from bot.database.db import create_user, get_user_by_telegram_id
from config import VALIDATOR_ID as vids, ADMIN_ID as aids

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
