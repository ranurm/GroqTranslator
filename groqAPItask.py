from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from groq import Groq

app = FastAPI()

# API Token (Environment Variable):
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set.")

# Initialize Groq client:
client = Groq(api_key=GROQ_API_KEY)

# Pydantic Model:
class TranslateRequest(BaseModel):
    text: str
    target_language: str

# FastAPI Endpoint:
@app.post("/translate/")
async def translate_text(request: TranslateRequest):
    try:
        # Construct the prompt dynamically:
        prompt = f"Translate the following text into {request.target_language}: {request.text}"

        # Groq API Call (Corrected):
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt # Use the constructed prompt
                }
            ],
            model="llama-3.3-70b-versatile"  # Or another appropriate Llama model
        )

        # Extract the translated text (Improved):
        translated_text = response.choices[0].message.content.strip()

        return {"translation": translated_text}

    except Exception as e:
        print(f"Error during translation: {e}")
        raise HTTPException(status_code=500, detail=f"Translation failed: {e}")