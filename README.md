# Jarvis - AI Voice Assistant

Jarvis is a voice-activated virtual assistant designed to perform various tasks such as web browsing, playing music, fetching news, and responding to user queries using gemini 1.5 flash api model.

## Features

### 🔊 Voice Recognition

- Utilizes the `speech_recognition` library to listen for and recognize voice commands.
- Activates upon detecting the wake word **"Jarvis."**

### 🗣️ Text-to-Speech

- Converts text to speech using `pyttsx3` for local conversion.
- Supports `gTTS` (Google Text-to-Speech) with `pygame` for playback.

### 🌐 Web Browsing

- Opens popular websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.

### 🎵 Music Playback

- Interfaces with a `musicLibrary` module to play songs via web links.

### 📰 News Fetching

- Fetches and reads the latest news headlines using **NewsAPI**.

### 🤖 Gemini AI Integration

- Handles complex queries and generates responses using Gemini's **1.5 flash model**.
- Acts as a general virtual assistant similar to Alexa or Google Assistant.
