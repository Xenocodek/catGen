import random

def promt_generator():
    CAT = 'cat'
    COLOR = ['black', 'white', 'red', 'gray', 'brown', 'striped', 'siamese', 'spotted']
    ACTION = ['jumping', 'running', 'playing', 'sleeping', 'seeking', 'climbing']
    CHARACTERISTICS = ['beautiful eyes', 'long moustache', 'long tail']

    random_color = random.choice(COLOR)
    random_action = random.choice(ACTION)
    random_char = random.choice(CHARACTERISTICS)

    return f"{CAT}, {random_color}, {random_action}, {random_char}, "