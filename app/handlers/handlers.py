from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.settings.lexicon import COMMANDS

router = Router()

@router.message(Command(COMMANDS['START']))
async def cmd_start(message: Message):
    await message.answer('Привет!')