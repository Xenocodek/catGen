from aiogram.types import BotCommand

from app.settings.lexicon import COMMANDS
from app.settings.config import Configuration

bot = Configuration().bot

async def set_main_menu(bot):
    main_menu_commands = [
        BotCommand(command=f"{COMMANDS['MAIN']}", 
                    description="Главное меню"),
        BotCommand(command=f"{COMMANDS['HELP']}", 
                    description="Справка по работе бота"),
        BotCommand(command=f"{COMMANDS['MYID']}", 
                    description="Узнать ID"),
        BotCommand(command=f"{COMMANDS['GEN']}", 
                    description="Сгенерировать картинку кота"),
        ]
    await bot.set_my_commands(main_menu_commands)