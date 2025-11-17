from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    DB_URL = "sqlite:///./confession.db"    

ANONYMITY_SALT = os.getenv("ANONYMITY_SALT")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

admin_ids_str = os.getenv("ADMIN_IDS")
ADMIN_IDS = [int(id_str.strip()) for id_str in admin_ids_str.split(",") if id_str.strip()]

validator_ids = os.getenv("VALIDATOR_IDS")
VALIDATOR_IDS = [int(id_str.strip()) for id_str in validator_ids.split(",") if id_str.strip()]

MIN_CONFESSION_LEN = 10
MAX_CONFESSION_LEN = 1000

COMMENTS_PER_PAGE = 10

LIKE_PTS = 1
DISLIKE_PTS = -1
