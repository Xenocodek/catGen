import os
import requests

from dotenv import load_dotenv
load_dotenv()

class TextToImageAPI:
    """A class that provides a method for generating images from text using an API."""
    def __init__(self):
        """Initializes the TextToImageAPI class and sets the API URL."""
        self.url = "https://stablediffusionapi.com/api/v3/text2img"

    def generate_image(self, prompt, width="512", height="512", samples="1", num_inference_steps="20", guidance_scale=7.5):
        """Sends a POST request to the API with the given prompt and other optional parameters to generate an image."""
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

        try:
            response = requests.post(self.url, headers=headers, json=payload)
            response.raise_for_status()
            response_json = response.json()
            
            if 'status' in response_json and response_json['status'] == 'error':
                # Проверяем наличие поля 'message' и его содержание
                if 'message' in response_json and 'monthly limit exceeded' in response_json['message'].lower():
                    ans = "Превышен ежемесячный лимит."
                else:
                    # Обработка других ошибок, если необходимо
                    ans = "Произошла ошибка: " + response_json.get('message', 'Не указано сообщение об ошибке')
            else:
                # Обработка успешного ответа
                ans = response_json['output'][0]
            return ans
        
        except requests.exceptions.RequestException as e:
            # Обработка ошибки связи с сервером
            ans = f"Произошла ошибка запроса {e}"
            return ans