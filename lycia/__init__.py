from lycia.config import Config
from pyrogram import Client

APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN

LYCIA = Client(':memory:', app_id=APP_ID, api_hash=API_HASH, bot_token=TOKEN)
