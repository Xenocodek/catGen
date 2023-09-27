import asyncio
import logging

from aiogram import Dispatcher

from app.handlers.handlers import router
from app.settings.config import conf


async def start():
    """
    Configure logging, create a bot instance, initialize a dispatcher,
    include the router, start polling, and close the bot session.
    """

    logging.basicConfig(
        level=conf.logging_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler('BOTLOG.log', encoding='utf-8'),
            logging.StreamHandler()
            ]
    )

    # Initialize a bot
    bot = conf.bot

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