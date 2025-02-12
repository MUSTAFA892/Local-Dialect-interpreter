from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
"""from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.schema import BaseOutputParser"""
import uvicorn

# Load environment variables from .env
load_dotenv()

# Set up FastAPI app
app = FastAPI()

# Add CORS middleware to handle cross-origin requests
origins = [
    "http://localhost",  # Localhost, adjust as needed for your local environment
    "http://localhost:8000",  # If running on this port locally
    "https://your-frontend-domain.com",
    "http://127.0.0.1:5000"  # Your public frontend domain (for production)
    # You can add more allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins to access your API
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Set up Gemini API key from environment variables
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Langmith tracking setup
"""os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")"""

# Define the Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """You are a Local Dialect Interpreter. You help translate informal local dialects into standard English in real-time, especially for non-native speakers or tourists. Your task is to identify the language of the dialect and provide the corresponding **figurative meaning or interpretation** of the expression in standard English. Only give me the name of the dialect language, followed by the figurative meaning or interpretation. Do not provide any extra explanation or information.
            Example:
            - Dialect: "Wassup, bro?"
            - Language: American English (Informal)
            - Figurative Meaning: "A casual greeting between friends."
            - Dialect: "Kahani suno"
            - Language: Hindi
            - Figurative Meaning: "Listen to the story."
            - Dialect: "Bandar kya jaane adrak ka swaad"
            - Language: Hindi
            - Figurative Meaning: "An inferior person cannot appreciate superior things." 
            """),
        ("user", "Question: {question}")
    ]
)

# Set up the Google Generative AI client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Request Body Model
class QuestionRequest(BaseModel):
    question: str

# Function to invoke the Google API and return the result
def get_google_ai_response(query):
    try:
        # Make sure to pass the prompt properly to the model invocation
        prompt_with_question = prompt.format(question=query)  # Format the prompt with the user query
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Model you want to use
            contents=prompt_with_question,
        )
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

# Custom Output Parser (optional if you want to modify how the output is structured)
def custom_output_parser(response_text):
    # You can add your custom parsing logic here if needed, for example, strip whitespace or split
    return response_text.strip()

# API endpoint to handle requests
@app.post("/generate-response")
async def generate_response(request: QuestionRequest):
    # Get the response from Google API
    result = get_google_ai_response(request.question)
    
    # Optionally parse the result if needed
    parsed_result = custom_output_parser(result)
    
    return {"response": parsed_result}

# To run the FastAPI app, use: uvicorn app:app --reload

if __name__ == "__main__":
    # Render expects the app to listen on 0.0.0.0 and port 10000
    port = 8000  # Use port 10000 (default for Render)
    uvicorn.run(app, host="0.0.0.0", port=port)
