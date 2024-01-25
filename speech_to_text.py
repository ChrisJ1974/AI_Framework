from openai import OpenAI
from config_module import Config

class SpeechToTextModule:
    def __init__(self):
        config = Config()
        self.client = OpenAI(api_key=config.get_openai_api_key)

    def transcribe_audio(self, audio_file_path, model="whisper-1", response_format="json"):
        with open(audio_file_path, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                model=model, 
                file=audio_file,
                response_format=response_format
            )
            return transcript

# Usage Example
if __name__ == "__main__":
    # Replace with your audio file path
    audio_file_path = "/path/to/your/audio/file.mp3"  

    speech_to_text = SpeechToTextModule()
    transcription = speech_to_text.transcribe_audio(audio_file_path)
    print(transcription)
