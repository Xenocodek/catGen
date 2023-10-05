#Importing libraries
from emoji import emojize

#Control buttons
KEYBOARD = {
    'MYID': "Узнать свой ID",
    'GEN': "Сгенерировать картинку кота", 
}

#Names of commands
COMMANDS = {
    'HELP': "help",
    'MYID': "my_id",
    'GEN': "gen",
    'SECRET': "secret",
}

MESSAGES = {
    'GREETINGS': emojize("👋 Привет, "),
    'EXCLAMATION_POINT': "!",
    'UNCLEAR': emojize("⁉ Я тебя не понимаю..."),
    'GET_USER_NAME': "Ваше имя: ",
    'GET_USER_ID': "Ваш ID: ",
    'PROMT': emojize("💬 Промт картинки: "),
    'AWAITING': emojize("🔄 Подождите... Картинка генерируется."),
    'SECRET_GIF': "CgACAgIAAxkBAAIB32UV9Bq-h_7DdNR19MkaiY75A7_ZAAKaNQACRamwSFQr5FWfN0tRMAQ",
}