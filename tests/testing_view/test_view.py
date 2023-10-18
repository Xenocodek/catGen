from app.handlers.view import is_url
from app.handlers.view import generate_image

class TestIsUrl:

    # Valid URL starting with http://
    def test_valid_url_starting_with_http(self):
        assert is_url("http://www.example.com") is True

    # Valid URL starting with https://
    def test_valid_url_https(self):
        assert is_url("https://www.example.com") is True

    # Valid URL with additional path and query parameters
    def test_valid_url_additional_parameters(self):
        assert is_url("https://www.example.com/path?param=value") is True

    # Empty string
    def test_empty_string(self):
        assert is_url("") is False

    # URL starting with ftp:// instead of http:// or https://
    def test_invalid_url_ftp(self):
        assert is_url("ftp://www.example.com") is False

    # URL with port number
    def test_url_with_port_number(self):
        assert is_url('http://example.com:8080') is True
        assert is_url('https://example.com:8080') is True
        assert is_url('ftp://example.com:8080') is False
        assert is_url('example.com:8080') is False

    # URL with only path
    def test_url_with_path_only(self):
        assert is_url('/path') is False

    # Non-URL text
    def test_non_url_text(self):
        assert is_url('This is not a URL') is False


class TestGenerateImage:
    
    # Generates an image based on a given prompt
    def test_generate_image_with_prompt(self):
        prompt = "Test prompt"
        result = generate_image(prompt)
        assert result is not None

    # Returns the generated image
    def test_generate_image_returns_image(self):
        prompt = "Test prompt"
        result = generate_image(prompt)
        assert isinstance(result, str)

    # Handles monthly limit exceeded error
    def test_generate_image_handles_monthly_limit_exceeded_error(self):
        prompt = "Test prompt"
        result = generate_image(prompt)
        assert result == "Превышен ежемесячный лимит."

        # Handles other API errors
    def test_generate_image_handles_other_api_errors(self):
        prompt = "Test prompt"
        result = generate_image(prompt)
        assert result.startswith("Произошла ошибка:")

    # Handles missing prompt parameter
    def test_generate_image_handles_missing_prompt_parameter(self):
        result = generate_image(None)
        assert result is None