from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Load OpenAI API Key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a request model to enforce JSON format
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using GPT-3.5 because GPT-4 isn't available for your key
            messages=[{"role": "user", "content": request.message}]
        )
        return {"response": response["choices"][0]["message"]["content"]}

    except Exception as e:
        return {"error": str(e)}