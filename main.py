from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import google.generativeai as genai

# 🔐 Configure your Gemini API Key
genai.configure(api_key="AIzaSyD3uZYBsydKEbpS6iEs-uQXeFjo3gHkm2g")  # 🔁 Replace this if needed

# 🚀 Initialize FastAPI app
app = FastAPI()

# 🌐 Allow frontend (Streamlit) to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-story")
async def generate_story(req: Request):
    try:
        data = await req.json()

        starter = data["starter"]
        genre = data["genre"]
        character = data.get("character", "A mysterious person")
        audience = data["audience"]

        prompt = (
            f"Write a creative story starting with:\n"
            f"{starter}\n\n"
            f"Genre: {genre}\n"
            f"Main Character: {character}\n"
            f"Target Audience: {audience}\n\n"
            f"Make sure to:\n"
            f"- Use simple words,dont use hard words, easy-to-understand language\n"
            f"- Write in paragraphs\n"
            f"- Highlight key lines with **bold**\n"
            f"- Start with a catchy title and title should be in **bold** and lil bigger in size\n"
            f"- it should be less than 270 words\n"
            f"- ending of story should be the completion of story\n"


        ) 


        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")  # Use full model name
        response = model.generate_content(prompt)


        if hasattr(response, "text"):
            story = response.text
            print("✅ Story generated successfully")
            return {"story": story}
        else:
            print("❌ Gemini returned no text")
            return {"error": "No story was generated."}

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return {"error": str(e)}
