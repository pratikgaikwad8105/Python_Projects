import requests
import io
import dotenv
import os

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")


def generate_speech(text, voice_id):

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return io.BytesIO(response.content)
    else:
        raise Exception(f"API Error: {response.json().get('error', 'Unknown error')}")
