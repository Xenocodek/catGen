import asyncio
import logging
from aiogram import Bot, Dispatcher
#from app.handlers import router
from app.settings.config import Config

TOKEN = Config.BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=Config.LOG_LEVEL,
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

async def main():
    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    #dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Bot stopped\n')