# AI Voice Assistant (Project Luna)

This is an open-source desktop voice assistant inspired by Siri/Alexa.
Built with Python + JavaScript to work on Windows, macOS, and Linux.

## Features
- Wake word detection
- Whisper STT
- Mixtral/GPT LLM
- TTS with Coqui/Pyttsx3
- Cross-platform system commands
AI Voice Assistant
A simple Python-based AI voice assistant that records your voice, transcribes it using OpenAI Whisper, and speaks back the recognized text.

Features
Record audio from your microphone

Transcribe speech to text with OpenAI Whisper

Text-to-speech response using pyttsx3

Requirements
Python 3.8 or higher

FFmpeg (for audio processing)

The following Python libraries:

openai-whisper

sounddevice

scipy

pyttsx3

numpy

Installation
1. Clone the Repository
bash
git clone https://github.com/yourusername/ai-voice-assistant.git
cd ai-voice-assistant
2. Set up a Virtual Environment (Recommended)
bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
3. Install Python Dependencies
bash
pip install openai-whisper sounddevice scipy pyttsx3 numpy
FFmpeg Installation
Windows
FFmpeg is required for audio processing by Whisper and other libraries.

Option 1: Using a Package Manager (Recommended)
Chocolatey:

bash
choco install ffmpeg
Winget:

bash
winget install ffmpeg
Scoop:

bash
scoop install ffmpeg
Option 2: Manual Installation
Download the latest FFmpeg build from gyan.dev.

Extract the archive (e.g., ffmpeg-release-essentials.zip).

Move the extracted folder to C:\ffmpeg.

Add C:\ffmpeg\bin to your Windows PATH environment variable:

Open "Edit the system environment variables".

Click "Environment Variables".

Under "System variables", select Path and click "Edit".

Click "New" and add C:\ffmpeg\bin.

Click "OK" to save.

Open a new Command Prompt and verify installation:

bash
ffmpeg -version
You should see FFmpeg version information.

Detailed guide with screenshots.

Linux / WSL
bash
sudo apt update
sudo apt install ffmpeg
Verify with:

bash
ffmpeg -version
Usage
Make sure your microphone and speakers are working (on Windows).

Run the assistant:

bash
python voice_loop.py
Speak when prompted. The assistant will transcribe and respond.

Troubleshooting
FFmpeg not found:
Ensure FFmpeg is installed and its bin directory is added to your system PATH.

Microphone not working in WSL:
WSL does not support direct audio hardware access. Run and test the project on Windows for audio features.

Contributing
Pull requests are welcome! Please ensure you have installed all dependencies and tested your changes on both Windows and Linux if possible.

License
MIT License