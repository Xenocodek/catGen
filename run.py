import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.handlers.handlers import router
from app.settings.config import Config

TOKEN = Config.BOT_TOKEN

async def start():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler('bot.log', encoding='utf-8'),
            logging.StreamHandler()
            ]
    )

    bot = Bot(TOKEN, parse_mode='HTML')

    dp = Dispatcher()

    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.info('Bot stopped\n')