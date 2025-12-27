from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

if not key:
    raise RuntimeError("OPENAI_API_KEY is not set")

client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input="Explain a random topic you find interesting"
)

print(response.output_text)
