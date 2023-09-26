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
}

MESSAGES = {
    'GREETINGS': "Привет, ",
    'EXCLAMATION_POINT': "!",
    'UNCLEAR': "Я тебя не понимаю...",
    'GET_USER_NAME': "Ваше имя: ",
    'GET_USER_ID': "Ваш ID: "
}