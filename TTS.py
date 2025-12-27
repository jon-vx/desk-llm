from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

if not key:
    raise RuntimeError("OPENAI_API_KEY is not set")

client = OpenAI()

audio_file = open("test.wav", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-mini-transcribe",
    file=audio_file
)

print(transcription.text)
