#Importing libraries
from emoji import emojize

#Version of the app
VERSION = '0.0.1'

#Author of the app
AUTHOR = 'Xenocode'

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
    'START': "start",
    'HELP': "help",
}