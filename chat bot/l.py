import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(api_key=os.getenv("API_KEY"))


tt = input("Welcome to chatbot, ask me: ")


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=tt
)


print(response.text)