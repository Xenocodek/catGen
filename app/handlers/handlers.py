from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.settings.lexicon import COMMANDS
from app.ai_gen.promt import promt_generator
from .events import *

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle the /start command."""
    await message.answer(greetings(message))

@router.message(Command(COMMANDS['MYID']))
async def cmd_my_id_name(message: Message):
    """A function that handles the /my_id_name command."""
    await message.answer(my_id_name(message))

@router.message(Command(COMMANDS['GEN']))
async def cmd_gen_image(message: Message):
    """Generates and sends an image as a reply to the user when they send the '/gen' command."""
    prompt = promt_generator()
    api_requests = generate_image(prompt)

    if is_url(api_requests):
        await message.answer_photo(api_requests, caption=f"{MESSAGES['PROMT']}{hbold(prompt)}")
    else:
        await message.answer(api_requests)

@router.message(Command(COMMANDS['SECRET']))
async def cmd_secret(message: Message):
    """Sends a secret GIF animation as a response to the user's message."""
    await message.answer_animation(f"{MESSAGES['SECRET_GIF']}")

@router.message()
async def cmd_unclear(message: Message):
    """A function that handles unclear commands."""
    await message.answer(f"{MESSAGES['UNCLEAR']}")