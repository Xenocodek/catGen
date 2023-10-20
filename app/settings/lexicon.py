#Importing libraries
from emoji import emojize

#Control buttons
KEYBOARD = {
    'MYID': emojize("🆔 Узнать свой ID"),
    'GEN': emojize("😺 Сгенерировать картинку кота"),
    'BACK_MAIN': emojize("↩️ Назад в главное меню"),
    'GEN_REPEAT': emojize("🐈 Сгенерировать картинку ещё раз"),
}

#Names of commands
COMMANDS = {
    'MAIN': "main",
    'HELP': "help",
    'MYID': "my_id",
    'GEN': "gen",
    'SECRET': "secret",
}

MESSAGES = {
    'GREETINGS': emojize("👋 Привет, "),
    'EXCLAMATION_POINT': "!",
    'REQUEST': 'Запрос принят!',
    'MAIN_MENU': emojize("🏠 Главное меню"),
    'UNCLEAR': emojize("⁉ Я тебя не понимаю..."),
    'GET_USER_NAME': emojize("👤 Ваше имя: "),
    'GET_USER_ID': emojize("🔑 Ваш ID: "),
    'PROMT': emojize("🐾 Промт картинки: "),
    'AWAITING': emojize("🔄 Подождите... Картинка генерируется."),
    'SECRET_GIF': "CgACAgIAAxkBAAIB32UV9Bq-h_7DdNR19MkaiY75A7_ZAAKaNQACRamwSFQr5FWfN0tRMAQ",
    'TEST': 'test'
}