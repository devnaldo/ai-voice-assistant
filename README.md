Voice Assistant: Speech-to-Text (Google STT) & Gemini AI
A Python-based voice assistant that records your speech, transcribes it using Google Speech-to-Text (STT), generates intelligent replies with Gemini AI, and speaks back the response—all locally on your machine.

Features
Voice Recording: Captures microphone audio and saves as WAV.

Speech Recognition: Uses Google STT API for accurate transcription.

Conversational AI: Integrates Gemini AI for natural language replies.

Text-to-Speech: Reads responses aloud using pyttsx3.

Keyboard Controls:

Press s to skip TTS playback.

Say "skip" or "exit" to control the session.

Secure API Key Handling:

Prompts for keys on first run, stores them in a local .env file (never committed).

Demo
bash
python voice_assistant.py
Requirements
Operating System: Windows, Linux, or macOS (audio features tested on Windows).

Python: 3.8 or higher.

Microphone and speakers for full functionality.

Installation
1. Clone the Repository
bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
2. Set Up a Virtual Environment (Recommended)
bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
requirements.txt

text
python-dotenv>=1.0.0
sounddevice>=0.4.6
scipy>=1.10.0
pyttsx3>=2.90
google-cloud-speech>=2.21.0
google-genai>=0.3.0
keyboard>=0.13.5
4. System Dependencies
PortAudio: Required for sounddevice.

Windows: Usually included with pip install.

Linux: Install with sudo apt-get install portaudio19-dev before installing requirements.

API Keys Setup
1. Gemini API Key
Get your Gemini API key from the Gemini developer portal.

On first run, you'll be prompted to paste your key. It will be saved in .env.

2. Google Speech-to-Text API Key
Create a project in Google Cloud Console.

Enable the Speech-to-Text API.

Create an API key.

On first run, paste your key when prompted. It will be saved in .env.

.env Example

text
GEMINI_API_KEY=your-gemini-key
GOOGLE_STT_API_KEY=your-google-key
Important:
.env is gitignored and never pushed to GitHub.

Usage
Start the assistant:

bash
python voice_assistant.py
Speak when prompted.

Say "exit" to quit, or "skip" to skip the Gemini reply.

Press s while the assistant is speaking to interrupt playback.

Security & Best Practices
API keys are never stored in code or committed to the repository.

Restrict your API keys in Google Cloud and Gemini dashboards to only necessary APIs and, if possible, to specific IPs.

Monitor usage, rotate keys regularly, and delete unused keys.

.env is gitignored by default.

Troubleshooting
Microphone not working?
Ensure your OS allows microphone access and that your device is selected as the default input.

Google STT errors?
Make sure your API key is valid and the Speech-to-Text API is enabled in your Google Cloud project.

Permission errors on Linux?
Try running as administrator or check audio group permissions.

Contribution
Pull requests are welcome! Please:

Test on your OS before submitting.

Never commit your .env or API keys.

Follow the code style and security guidelines.

License
MIT License

