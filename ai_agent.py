from fastapi import FastAPI
import openai
import os

app = FastAPI()

# Ensure OpenAI API Key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found! Set OPENAI_API_KEY in environment variables.")

client = openai.Client(api_key=api_key)

@app.get("/")
def read_root():
    return {"message": "AI Agent is running!"}

@app.get("/chat")
def chat(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"response": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}  # Return actual error message
