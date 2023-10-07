from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.settings.config import Configuration
from app.settings.lexicon import COMMANDS

from .events import *

bot = Configuration().bot
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle the /start command."""
    await greetings(message)

@router.message(Command(COMMANDS['MAIN']))
async def cmd_start(message: Message):
    """Handle the /main command."""
    await greetings(message)

@router.message(Command(COMMANDS['MYID']))
async def cmd_my_id_name(message: Message):
    """A function that handles the /my_id_name command."""
    await my_id_name(message)

@router.message(Command(COMMANDS['GEN']))
async def handle_gen_cmd(message: Message):
    """Generate a image"""
    await cmd_gen_image(message)

@router.message(Command(COMMANDS['SECRET']))
async def cmd_secret(message: Message):
    """Sends a secret GIF animation as a response to the user's message."""
    await message.answer_animation(f"{MESSAGES['SECRET_GIF']}")

@router.callback_query(F.data == 'MYID')
async def callback_my_id_name(callback: CallbackQuery):
    """A callback function that handles the callback query with data field equal to 'MYID'."""
    await my_id_name_from_callback(callback)

@router.callback_query(F.data == 'GEN')
async def handle_gen_callback(callback: CallbackQuery):
    """Handle the callback query for 'GEN' data."""
    await callback_gen_image(callback)

@router.callback_query(F.data == 'GEN_REPEAT')
async def handle_gen_callback(callback: CallbackQuery):
    """Handle the callback query for 'GEN_REPEAT' data."""
    await callback_gen_image_repeat(callback)

@router.callback_query(F.data == 'BACK_MAIN')
async def handle_back_menu_callback(callback: CallbackQuery):
    """A function that handles the 'BACK_MAIN' callback query."""
    await callback_back_menu(callback)

@router.message()
async def cmd_unclear(message: Message):
    """A function that handles unclear commands."""
    await message.answer(f"{MESSAGES['UNCLEAR']}")