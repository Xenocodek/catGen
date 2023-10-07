import re

from aiogram.utils.markdown import hbold
from aiogram.types import Message, CallbackQuery

from app.settings.lexicon import MESSAGES
from app.ai_gen.text2image import TextToImageAPI



from app.ai_gen.promt import promt_generator
from app.keyboards.inlinekb import (start_keyboard, 
                                    after_gen_keyboard)

from app.settings.config import Configuration
conf = Configuration()
bot = conf.bot


def get_first_name(message: Message):
    """Returns the user's first name from a Message."""
    return message.from_user.first_name

def get_full_name(message: Message):
    """Returns the user's full name from a Message."""
    return message.from_user.full_name

def get_id(message: Message):
    """Returns the user's ID from a Message."""
    return message.from_user.id

def greetings(message: Message):
    """Returns a formatted greeting message with the user's first name."""
    name = get_first_name(message)
    return f"{MESSAGES['GREETINGS']}{hbold(name)}{MESSAGES['EXCLAMATION_POINT']}"

def my_id_name(message: Message):
    """Construct a message string using the user's full name and ID from the given Message object."""
    user_name = get_full_name(message)
    user_id = get_id(message)
    message = (
        f"{MESSAGES['GET_USER_NAME']}{hbold(user_name)}\n"
        f"{MESSAGES['GET_USER_ID']}{hbold(user_id)}"
    )
    return message

def my_id_name_from_callback(callback: CallbackQuery):
    """Generates a message containing the user's name and ID from a callback query."""
    user = callback.from_user
    user_name = user.full_name
    user_id = user.id
    message = (
        f"{MESSAGES['GET_USER_NAME']}{hbold(user_name)}\n"
        f"{MESSAGES['GET_USER_ID']}{hbold(user_id)}"
    )
    return message

def is_url(text):
    """Check if a given text is a URL."""
    return re.match(r'https?://', text) is not None

def generate_image(prompt):
    """Generates an image based on a given prompt using the TextToImageAPI class."""
    return TextToImageAPI().generate_image(prompt)

async def cmd_gen_image(message: Message):
    """Generates and sends an image based on a prompt."""
    reply_message = await message.reply(f"{MESSAGES['AWAITING']}")
    
    prompt = promt_generator()
    api_requests = generate_image(prompt)
    
    if is_url(api_requests):
        caption = f"{MESSAGES['PROMT']}{hbold(prompt)}"
        await message.answer_photo(photo=api_requests, caption=caption)
    else:
        await message.answer(api_requests)
    
    await bot.delete_message(message.from_user.id, reply_message.message_id)

async def callback_gen_image(callback: CallbackQuery):
    """Function to handle the callback query with data 'GEN' from the router."""
    reply_message = await callback.message.answer(f"{MESSAGES['AWAITING']}")
    
    prompt = promt_generator()
    api_requests = generate_image(prompt)
    
    if is_url(api_requests):
        caption = f"{MESSAGES['PROMT']}{hbold(prompt)}"
        photo_message = await callback.message.answer_photo(photo=api_requests, caption=caption, reply_markup=after_gen_keyboard)
    else:
        await callback.answer(api_requests, reply_markup=after_gen_keyboard)
        photo_message = None
    
    if photo_message:
        await bot.delete_message(callback.from_user.id, reply_message.message_id)

async def callback_gen_image_repeat(callback: CallbackQuery):
    """Function to handle the callback query with data 'GEN' from the router."""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
    
    reply_message = await callback.message.answer(f"{MESSAGES['AWAITING']}")
    prompt = promt_generator()
    api_requests = generate_image(prompt)
    
    if is_url(api_requests):
        caption = f"{MESSAGES['PROMT']}{hbold(prompt)}"
        await callback.message.answer_photo(photo=api_requests, caption=caption,
                                            reply_markup=after_gen_keyboard)
    else:
        await callback.answer(api_requests, reply_markup=after_gen_keyboard)
    
    await bot.delete_message(callback.from_user.id, reply_message.message_id)

async def callback_back_menu(callback: CallbackQuery):
    """Asynchronous function that handles the callback from the back menu button."""
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )

    await callback.message.answer(
        f"{hbold(MESSAGES['MAIN_MENU'])}",
        reply_markup=start_keyboard
    )