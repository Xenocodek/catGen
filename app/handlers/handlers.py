from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.markdown import hbold

from app.settings.messages import GREETINGS, EXCLAMATION_POINT

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Handle the /start command.
    """
    await message.answer(f"{GREETINGS}{hbold(message.from_user.first_name)}{EXCLAMATION_POINT}")