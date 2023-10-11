from aiogram.utils.markdown import hbold
from aiogram.types import Message, CallbackQuery

from app.settings.lexicon import MESSAGES
from .view import *

from app.ai_gen.promt import promt_generator
from app.keyboards.inlinekb import (start_keyboard,
                                    after_get_id_keyboard, 
                                    after_gen_keyboard)

from app.settings.config import Configuration

bot = Configuration().bot

async def greetings(message: Message):
    """Returns a formatted greeting message with the user's first name."""
    user_name = message.from_user.first_name
    response = f"{MESSAGES['GREETINGS']}{hbold(user_name)}{MESSAGES['EXCLAMATION_POINT']}"
    await message.answer(response, reply_markup=start_keyboard)

async def my_id_name(message: Message):
    """Construct a message string using the user's full name and ID from the given Message object."""
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    message_name_id = (
        f"{MESSAGES['GET_USER_NAME']}{hbold(user_name)}\n"
        f"{MESSAGES['GET_USER_ID']}{hbold(user_id)}"
    )
    await message.answer(message_name_id)

async def my_id_name_from_callback(callback: CallbackQuery):
    """Generates a message containing the user's name and ID from a callback query."""
    await callback.answer()
    
    await bot.delete_message(callback.from_user.id, callback.message.message_id)

    user = callback.from_user
    user_name = user.full_name
    user_id = user.id
    message_name_id = (
        f"{MESSAGES['GET_USER_NAME']}{hbold(user_name)}\n"
        f"{MESSAGES['GET_USER_ID']}{hbold(user_id)}"
    )
    await callback.message.answer(message_name_id, reply_markup=after_get_id_keyboard)

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
    await callback.answer(MESSAGES['REQUEST'])
    
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    
    reply_message = await callback.message.answer(f"{MESSAGES['AWAITING']}")
    
    prompt = promt_generator()
    api_requests = generate_image(prompt)
    
    if is_url(api_requests):
        caption = f"{MESSAGES['PROMT']}{hbold(prompt)}"
        photo_message = await callback.message.answer_photo(photo=api_requests, caption=caption, 
                                                            reply_markup=after_gen_keyboard)
    else:
        await callback.answer(api_requests, reply_markup=after_gen_keyboard)
        photo_message = None
    
    if photo_message:
        await bot.delete_message(callback.from_user.id, reply_message.message_id)

async def callback_gen_image_repeat(callback: CallbackQuery):
    """Function to handle the callback query with data 'GEN' from the router."""
    await callback.answer(MESSAGES['REQUEST'])
    
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
    await callback.answer()

    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )

    await callback.message.answer(
        f"{hbold(MESSAGES['MAIN_MENU'])}",
        reply_markup=start_keyboard
    )