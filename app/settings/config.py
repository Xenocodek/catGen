import os
import logging
from aiogram import Bot
from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()

@dataclass
class BotConfig:
    """Bot configuration."""

    token: str = os.getenv("API_TOKEN")
    admin_id: int = os.getenv("ADMIN_ID")


@dataclass
class Configuration:
    """All in one configuration's class."""

    logging_level = int(os.getenv('LOGGING_LEVEL', logging.INFO))

    botconfig = BotConfig()

    bot = Bot(token=botconfig.token, parse_mode='HTML')