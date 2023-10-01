from aiogram.utils.markdown import hbold
from aiogram.types import Message

from app.settings.lexicon import MESSAGES
from app.ai_gen.text2image import TextToImageAPI


def get_first_name(message: Message):
    """Returns the user's first name."""
    return message.from_user.first_name

def get_full_name(message: Message):
    """Returns the user's full name."""
    return message.from_user.full_name

def get_id(message: Message):
    """Returns the user's ID."""
    return message.from_user.id

def greetings(message: Message):
    """Returns a formatted greeting message with the user's first name."""
    name = get_first_name(message)
    return f"{MESSAGES['GREETINGS']}{hbold(name)}{MESSAGES['EXCLAMATION_POINT']}"

def my_id_name(message: Message):
    """Construct a message string using the user's full name and ID from the given Message object."""
    name = get_full_name(message)
    id = get_id(message)
    message = (
        f"{MESSAGES['GET_USER_NAME']}{hbold(name)}\n"
        f"{MESSAGES['GET_USER_ID']}{hbold(id)}"
    )
    return message

def generate_image(prompt):
    """Generates an image based on a given prompt using the TextToImageAPI class."""
    imgGen = TextToImageAPI()
    result = imgGen.generate_image(prompt)
    return result