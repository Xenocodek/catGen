import re

from app.ai_gen.text2image import TextToImageAPI

def is_url(text):
    """Check if a given text is a URL."""
    return re.match(r'https?://', text) is not None

def generate_image(prompt):
    """Generates an image based on a given prompt using the TextToImageAPI class."""
    return TextToImageAPI().generate_image(prompt)