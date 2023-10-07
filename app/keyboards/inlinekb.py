from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.settings.lexicon import KEYBOARD

def create_inline_kb(width, *args, **kwargs):
    """ Generate a custom inline keyboard with the specified width and buttons."""
    kb_builder = InlineKeyboardBuilder()
    buttons = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=KEYBOARD[button] if button in KEYBOARD else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
            
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()

# Create start keyboard with inline buttons for 'MYID' and 'GEN'
start_keyboard = create_inline_kb(1, 'MYID', 'GEN')
# Create keyboard after getting the ID with an inline button for 'BACK_MAIN'
after_get_id_keyboard = create_inline_kb(1, 'BACK_MAIN')
# Create keyboard after generating something with inline buttons for 'GEN_REPEAT' and 'BACK_MAIN'
after_gen_keyboard = create_inline_kb(1, 'GEN_REPEAT', 'BACK_MAIN')