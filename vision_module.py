# vision_module.py
import openai
import base64
import logging
from config_module import Config

class VisionModule:
    def __init__(self):
        config = Config()
        self.api_key = config.openai_api_key  # Accessing as an attribute
        openai.api_key = self.api_key
        logging.basicConfig(level=logging.INFO)

    def encode_image(self, image_path):
        """Encodes an image to base64."""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except FileNotFoundError:
            logging.error(f"File not found: {image_path}")
            return None

    def analyze_image(self, image_paths, use_base64=False):
        """Analyzes multiple images using OpenAI's API."""
        images = []
        for path in image_paths:
            if use_base64:
                encoded_image = self.encode_image(path)
                if encoded_image:
                    images.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}})
            else:
                images.append({"type": "image_url", "image_url": {"url": path}})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": images
                    }
                ],
                max_tokens=300
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Error in OpenAI API call: {e}")
            return None

# Example usage
vision_module = VisionModule()
