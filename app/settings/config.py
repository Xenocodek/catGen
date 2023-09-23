import os
from dataclasses import dataclass

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str = os.getenv("API_TOKEN")
    ADMIN_ID: int = os.getenv("ADMIN_ID")

bot = Bot(token=Config.BOT_TOKEN, parse_mode='HTML')