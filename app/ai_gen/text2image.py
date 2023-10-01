import os
import requests
import json

from dotenv import load_dotenv
load_dotenv()

class TextToImageAPI:
    def __init__(self):
        self.url = "https://stablediffusionapi.com/api/v3/text2img"

    def generate_image(self, prompt, width="512", height="512", samples="1", num_inference_steps="20", guidance_scale=7.5):
        payload = {
            "key": os.getenv("API_TOKEN_SD"),
            "prompt": prompt,
            "negative_prompt": None,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "seed": None,
            "guidance_scale": guidance_scale,
            "safety_checker": "yes",
            "multi_lingual": "no",
            "panorama": "no",
            "self_attention": "no",
            "upscale": "no",
            "embeddings_model": None,
            "webhook": None,
            "track_id": None
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self.url, headers=headers, json=payload)
        response_json = response.json()
        return response_json

# Пример использования класса

imgGen = TextToImageAPI()
prompt = "cat, black"
result = imgGen.generate_image(prompt)
print(result)