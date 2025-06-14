import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import logging

# Suppress verbose logs
logging.getLogger('pyttsx3').setLevel(logging.ERROR)

# Config
SAMPLE_RATE = 16000
DURATION = 5  # seconds
FILENAME = "input.wav"

# Load Whisper model once
model = whisper.load_model("base")

def record_audio():
    print("🎙️ Listening for 5 seconds...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write(FILENAME, SAMPLE_RATE, audio)
    print("✅ Audio recorded.")

def transcribe_audio():
    result = model.transcribe(FILENAME)
    print("📝 You said:", result["text"])
    return result["text"]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    record_audio()
    text = transcribe_audio()
    speak("You said: " + text)
