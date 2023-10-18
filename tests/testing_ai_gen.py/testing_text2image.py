from app.ai_gen.text2image import TextToImageAPI

class TestTextToImageAPI:

    # Generates an image with default parameters
    def test_generate_image_default_parameters(self):
        api = TextToImageAPI()
        prompt = "Generate image with default parameters"
        result = api.generate_image(prompt)
        assert result is not None

    # Generates an image with custom width and height
    def test_generate_image_custom_width_height(self):
        api = TextToImageAPI()
        prompt = "Generate image with custom width and height"
        width = "800"
        height = "600"
        result = api.generate_image(prompt, width=width, height=height)
        assert result is not None

    # Generates an image with multiple samples
    def test_generate_image_multiple_samples(self):
        api = TextToImageAPI()
        prompt = "Generate image with multiple samples"
        samples = "5"
        result = api.generate_image(prompt, samples=samples)
        assert result is not None

    # Generates an image with custom guidance scale
    def test_generate_image_custom_guidance_scale(self):
        api = TextToImageAPI()
        prompt = "Generate image with custom guidance scale"
        guidance_scale = 10.0
        result = api.generate_image(prompt, guidance_scale=guidance_scale)
        assert result is not None

    # Generates an image with a prompt containing special characters
    def test_generate_image_special_characters_prompt(self):
        api = TextToImageAPI()
        prompt = "Generate image with special characters: !@#$%^&*()"
        result = api.generate_image(prompt)
        assert result is not None

    # Generates an image with the minimum width and height values (1x1)
    def test_generate_image_minimum_width_height(self):
        api = TextToImageAPI()
        prompt = "Generate image with minimum width and height"
        width = "1"
        height = "1"
        result = api.generate_image(prompt, width=width, height=height)
        assert result is not None

    # Generates an image with the maximum width and height values (4096x4096)
    def test_generate_image_maximum_width_height(self):
        api = TextToImageAPI()
        prompt = "Generate image with maximum width and height"
        width = "4096"
        height = "4096"
        result = api.generate_image(prompt, width=width, height=height)
        assert result is not None

    # Generates an image with the minimum number of inference steps (1)
    def test_generate_image_minimum_inference_steps(self):
        api = TextToImageAPI()
        prompt = "Generate image with minimum inference steps"
        num_inference_steps = "1"
        result = api.generate_image(prompt, num_inference_steps=num_inference_steps)
        assert result is not None

    # Generates an image with the maximum number of inference steps (100)
    def test_generate_image_maximum_inference_steps(self):
        api = TextToImageAPI()
        prompt = "Generate image with maximum inference steps"
        num_inference_steps = "100"
        result = api.generate_image(prompt, num_inference_steps=num_inference_steps)
        assert result is not None

    # Generates an image with the minimum guidance scale value (0.1)
    def test_generate_image_minimum_guidance_scale(self):
        api = TextToImageAPI()
        prompt = "Generate image with minimum guidance scale"
        guidance_scale = 0.1
        result = api.generate_image(prompt, guidance_scale=guidance_scale)
        assert result is not None