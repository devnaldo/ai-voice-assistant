import os
import threading
from dotenv import load_dotenv
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import pyttsx3
from google import genai
import keyboard

# ========== Load or Get API Key ==========
load_dotenv()  # Load existing .env file

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("⚠️ Gemini API key not found!")
    api_key = input("👉 Please paste your Gemini API key: ").strip()
    with open(".env", "a") as env_file:
        env_file.write(f"\nGEMINI_API_KEY={api_key}")
    print("✅ API key saved to .env for future runs.")

# Initialize Gemini client
genai_client = genai.Client(api_key=api_key)

# ========== Constants ==========
SAMPLE_RATE = 16000
DURATION = 5  # seconds
FILENAME = "input.wav"

# ========== Voice Recording ==========
def record_audio():
    print("🎙️ Listening for 5 seconds...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write(FILENAME, SAMPLE_RATE, audio)
    print("✅ Audio recorded.")

# ========== Transcription ==========
model = whisper.load_model("base")
def transcribe_audio():
    result = model.transcribe(FILENAME)
    print("📝 You said:", result["text"])
    return result["text"]

# ========== Gemini AI Reply ==========
def get_gemini_reply(prompt):
    response = genai_client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    print("🤖 Gemini says:", response.text)
    return response.text

# ========== TTS with Skip Support ==========
def speak_response(text):
    engine = pyttsx3.init()
    stop_flag = threading.Event()

    def check_for_skip():
        keyboard.wait('s')
        print("⏹️ Speech interrupted by 's' key.")
        stop_flag.set()
        engine.stop()

    skip_thread = threading.Thread(target=check_for_skip)
    skip_thread.start()

    engine.say(text)
    engine.runAndWait()

    stop_flag.set()

# ========== Main Loop ==========
if __name__ == "__main__":
    print("🤖 Voice Assistant Started!")
    print("Say 'exit' to quit or 'skip' to skip reply.")
    print("Press 's' key while AI is speaking to interrupt.\n")

    while True:
        record_audio()
        user_input = transcribe_audio()

        if any(word in user_input.lower() for word in ["exit", "quit", "bye", "stop"]):
            print("👋 Exiting. Goodbye!")
            speak_response("Goodbye!")
            break

        if any(word in user_input.lower() for word in ["skip", "ignore", "next"]):
            print("⏭️ Skipping Gemini response and TTS.")
            continue

        reply = get_gemini_reply(user_input)
        speak_response(reply)
