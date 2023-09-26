from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.markdown import hbold

from app.settings.lexicon import *

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Handle the /start command.
    """
    await message.answer(f"{MESSAGES['GREETINGS']}{hbold(message.from_user.first_name)}{MESSAGES['EXCLAMATION_POINT']}")