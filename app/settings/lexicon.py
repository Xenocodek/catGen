#Importing libraries
from emoji import emojize

#Control buttons
KEYBOARD = {
    'SETTINGS': emojize('⚙️ Настройки'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
}

#Names of commands
COMMANDS = {
    'HELP': "help",
    'MYID': "my_id",
    'GEN': "gen",
    'SECRET': "secret",
}

MESSAGES = {
    'GREETINGS': "Привет, ",
    'EXCLAMATION_POINT': "!",
    'UNCLEAR': "Я тебя не понимаю...",
    'GET_USER_NAME': "Ваше имя: ",
    'GET_USER_ID': "Ваш ID: ",
    'PROMT': "Промт картинки: ",
    'SECRET_GIF': "CgACAgIAAxkBAAIB32UV9Bq-h_7DdNR19MkaiY75A7_ZAAKaNQACRamwSFQr5FWfN0tRMAQ",
}