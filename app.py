import streamlit as st
import threading
import uvicorn
import time
from backend import app as fastapi_app
import requests

# Start FastAPI backend in a separate thread
def start_backend():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000)

threading.Thread(target=start_backend, daemon=True).start()
time.sleep(1)  

st.set_page_config(page_title="HR Chatbot", layout="wide")
st.title("HR Resource Query Chatbot")

query = st.text_input("Ask about employees (e.g., 'Find Python developers with AWS experience')")

if query:
    try:
        response = requests.get("http://127.0.0.1:8000/employees/search", params={"query": query})
        data = response.json()
        results = data.get("results", [])

        if not results:
            st.warning("No matching employees found.")
        else:
            from rag import RAGChatbot
            chatbot = RAGChatbot(results)
            natural_response = chatbot.generate_response(query)
            st.markdown(natural_response)
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
