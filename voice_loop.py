import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import os
from datetime import datetime

SAMPLE_RATE = 16000
DURATION = 5  # seconds
model = whisper.load_model("tiny")
def record_audio(filename="input.wav"):
    print("🎙️ Listening for 5 seconds...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write(filename, SAMPLE_RATE, audio)
    print("✅ Audio recorded.")

def transcribe_audio(filename="input.wav"):
    result = model.transcribe(filename)
    print("📝 Transcription:", result["text"])
    return result["text"]

def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_reply(text):
    text = text.lower()
    if "your name" in text:
        return "I am your voice assistant."
    elif "how are you" in text:
        return "I am doing great, thank you!"
    elif "time" in text:
        return "The current time is " + datetime.now().strftime("%I:%M %p")
    else:
        return "Sorry, I didn't understand that."

if __name__ == "__main__":
    record_audio()
    text = transcribe_audio()
    reply = get_reply(text)
    speak_response(reply)
