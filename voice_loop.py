import os
import threading
from dotenv import load_dotenv
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import assemblyai as aai  # Added AssemblyAI
import keyboard
from google import genai  # Keep Gemini for AI responses

# ========== Load or Get API Keys ==========
load_dotenv()

# Gemini API Key
GEMINI_API_KEY_NAME = "GEMINI_API_KEY"
gemini_api_key = os.getenv(GEMINI_API_KEY_NAME)
if not gemini_api_key:
    print("⚠️ Gemini API key not found!")
    gemini_api_key = input("👉 Please paste your Gemini API key: ").strip()
    with open(".env", "a") as env_file:
        env_file.write(f"\n{GEMINI_API_KEY_NAME}={gemini_api_key}")
    print("✅ Gemini API key saved to .env for future runs.")

# AssemblyAI API Key
ASSEMBLYAI_API_KEY_NAME = "ASSEMBLYAI_API_KEY"
assemblyai_api_key = os.getenv(ASSEMBLYAI_API_KEY_NAME)
if not assemblyai_api_key:
    print("⚠️ AssemblyAI API key not found!")
    assemblyai_api_key = input("👉 Please paste your AssemblyAI API key: ").strip()
    with open(".env", "a") as env_file:
        env_file.write(f"\n{ASSEMBLYAI_API_KEY_NAME}={assemblyai_api_key}")
    print("✅ AssemblyAI API key saved to .env for future runs.")

# Configure AssemblyAI
aai.settings.api_key = assemblyai_api_key

# Initialize Gemini client
genai_client = genai.Client(api_key=gemini_api_key)

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

# ========== AssemblyAI Transcription ==========
def transcribe_audio():
    print("🔍 Transcribing with AssemblyAI...")
    transcriber = aai.Transcriber()
    
    try:
        transcript = transcriber.transcribe(FILENAME)
        if transcript.status == aai.TranscriptStatus.error:
            print(f"❌ Transcription error: {transcript.error}")
            return ""
            
        text = transcript.text
        if not text:
            print("📝 No speech detected.")
            return ""
            
        print("📝 You said:", text)
        return text
        
    except Exception as e:
        print(f"❌ Transcription failed: {str(e)}")
        return ""

# ========== Gemini AI Reply ==========
def get_gemini_reply(prompt):
    response = genai_client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    print("🤖 Gemini says:", response.text)
    return response.text

# ========== TTS with Skip Support ==========
def speak_response(text, is_exit=False):
    engine = pyttsx3.init()
    stop_flag = threading.Event()

    def check_for_skip():
        print("⏳ You can press 's' to skip...")
        while not stop_flag.is_set():
            if keyboard.is_pressed('s'):
                print("⏹️ Speech interrupted by 's' key.")
                stop_flag.set()
                engine.stop()
                break

    if not is_exit:
        skip_thread = threading.Thread(target=check_for_skip)
        skip_thread.start()

    engine.say(text)
    engine.runAndWait()

    stop_flag.set()
    if not is_exit:
        skip_thread.join()

# ========== Main Loop ==========
if __name__ == "__main__":
    print("🤖 Voice Assistant Started! (Using AssemblyAI for STT)")
    print("Say 'exit' to quit or 'skip' to skip reply.")
    print("Press 's' key while AI is speaking to interrupt.\n")

    while True:
        record_audio()
        user_input = transcribe_audio()

        if any(word in user_input.lower() for word in ["exit", "quit", "bye", "stop"]):
            print("👋 Exiting. Goodbye!")
            speak_response("Goodbye!", is_exit=True)
            break

        if any(word in user_input.lower() for word in ["skip", "ignore", "next"]):
            print("⏭️ Skipping Gemini response and TTS.")
            continue

        reply = get_gemini_reply(user_input)
        speak_response(reply)
