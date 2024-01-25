import openai
from pathlib import Path

class TextToSpeech:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_speech(self, text, voice='alloy', model='tts-1', output_format='mp3', output_file='speech.mp3'):
        try:
            response = openai.Audio.speech.create(
                model=model,
                voice=voice,
                input=text,
                response_format=output_format
            )

            # Save the audio file
            with open(output_file, 'wb') as file:
                file.write(response['data'])
            print(f"Audio file saved as {output_file}")

        except Exception as e:
            print(f"An error occurred: {e}")

# Usage
if __name__ == "__main__":
    api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API Key
    tts = TextToSpeech(api_key)
    tts.generate_speech("Today is a wonderful day to build something people love!")

