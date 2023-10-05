import re

from aiogram.utils.markdown import hbold
from aiogram.types import Message, CallbackQuery

from app.settings.lexicon import MESSAGES
from app.ai_gen.text2image import TextToImageAPI


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
    imgGen = TextToImageAPI()
    result = imgGen.generate_image(prompt)
    return result