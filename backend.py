# backend.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from rag import RAGChatbot
import json

# Load employees
with open("dataset.json", "r") as f:
    data = json.load(f)
employees = data["employees"]

chatbot = RAGChatbot(employees)

app = FastAPI(title="HR Resource Query API")

# Enable CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/employees/search")
def search_employees(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    results = chatbot.search(query)
    return {"query": query, "results": results}
