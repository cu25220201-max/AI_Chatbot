from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_response(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"