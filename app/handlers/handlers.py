from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.settings.config import Configuration
from app.settings.lexicon import COMMANDS
from app.ai_gen.promt import promt_generator
from app.keyboards.inlinekb import (start_keyboard, 
                                    after_get_id_keyboard)
from .events import *

conf = Configuration()
bot = conf.bot
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle the /start command."""
    await message.answer(greetings(message), reply_markup=start_keyboard)

@router.message(Command(COMMANDS['MAIN']))
async def cmd_start(message: Message):
    await message.answer(greetings(message), reply_markup=start_keyboard)

@router.message(Command(COMMANDS['MYID']))
async def cmd_my_id_name(message: Message):
    """A function that handles the /my_id_name command."""
    await message.answer(my_id_name(message))

@router.message(Command(COMMANDS['GEN']))
async def handle_gen_cmd(message: Message):
    await cmd_gen_image(message)

@router.message(Command(COMMANDS['SECRET']))
async def cmd_secret(message: Message):
    """Sends a secret GIF animation as a response to the user's message."""
    await message.answer_animation(f"{MESSAGES['SECRET_GIF']}")

@router.callback_query(F.data == 'MYID')
async def callback_my_id_name(callback: CallbackQuery):
    """A callback function that handles the callback query with data field equal to 'MYID'."""
    await callback.answer()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer(my_id_name_from_callback(callback), reply_markup=after_get_id_keyboard)

@router.callback_query(F.data == 'GEN')
async def handle_gen_callback(callback: CallbackQuery):
    await callback.answer("Запрос принят!")
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback_gen_image(callback)

@router.callback_query(F.data == 'GEN_REPEAT')
async def handle_gen_callback(callback: CallbackQuery):
    await callback.answer("Запрос принят!")
    await callback_gen_image_repeat(callback)

@router.callback_query(F.data == 'BACK_MAIN')
async def handle_back_menu_callback(callback: CallbackQuery):
    await callback.answer()
    await callback_back_menu(callback)

@router.message()
async def cmd_unclear(message: Message):
    """A function that handles unclear commands."""
    await message.answer(f"{MESSAGES['UNCLEAR']}")