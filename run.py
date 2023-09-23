import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.handlers.handlers import router
from app.settings.config import Config

TOKEN = Config.BOT_TOKEN

async def start():
    """
    Configure logging, create a bot instance, initialize a dispatcher,
    include the router, start polling, and close the bot session.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler('bot.log', encoding='utf-8'),
            logging.StreamHandler()
            ]
    )

    # Create a bot instance
    bot = Bot(TOKEN, parse_mode='HTML')

    # Initialize a dispatcher
    dp = Dispatcher()

    # Include the router
    dp.include_router(router)

    try:
        # Start polling
        await dp.start_polling(bot)
    finally:
        # Close the bot session
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.info('Bot stopped\n')