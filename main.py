"""
Support Intelligence Assistant - Main Application Server
Built for Wealthsimple AI Builder submission
Author: Williams Agbo
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from chatbot import get_bot_response

# Initialize FastAPI
app = FastAPI(title="Support Intelligence Assistant", 
              description="AI-powered ticket triage with human oversight",
              version="1.0.0")

# Enable CORS so frontend can talk to backend
# I learned about CORS the hard way during development!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request/response models
class ChatRequest(BaseModel):
    message: str
    ticket_type: str = "general"

class ChatResponse(BaseModel):
    reply: str
    category: str
    priority: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """
    Serve the main HTML interface.
    I wanted to keep everything simple for the demo.
    """
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/support", response_model=ChatResponse)
async def support_ticket(request: ChatRequest):
    """
    Process a support ticket and return AI analysis.
    This endpoint handles categorization and routing.
    """
    try:
        # Get response from our logic layer
        # In production, this could be swapped for any LLM
        result = await get_bot_response(request.message)
        return result
    except Exception as e:
        # Fail gracefully - always return something useful
        return {
            "reply": f"System is processing your request. A human will review shortly.",
            "category": "general",
            "priority": "low"
        }

# Health check endpoint - good practice for APIs
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "support-intelligence-assistant"}

# Run with: uvicorn main:app --reload --port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)