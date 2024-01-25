# main.py
from vision_module import VisionModule
from text_to_speech import VoiceModule
from speech_to_text import SpeechToTextModule
from data_interpreter_module import DataInterpreterModule
from calculation_module import CalculationModule


def main():
    vision_module = VisionModule()
    voice_module = VoiceModule()
    data_interpreter_module = DataInterpreterModule()
    calculation_module = CalculationModule()

    # Example usage of each module
    vision_result = vision_module.analyze_image('path/to/your/image.jpg')
    tts_result = voice_module.text_to_speech("Hello, World!")
    stt_result = voice_module.speech_to_text("path/to/audio/file.wav")
    interpreter_result = data_interpreter_module.interpret_data("Sample data to interpret")

    print("Vision Module Result:", vision_result)
    print("Text-to-Speech Result:", tts_result)
    print("Speech-to-Text Result:", stt_result)
    print("Data Interpreter Module Result:", interpreter_result)
    

if __name__ == "__main__":
    main()
