# HR Resource Query Chatbot

## 1. Overview
The HR Resource Query Chatbot is an AI-powered system that helps HR teams quickly find employees based on skills, experience, and project history. It uses a **RAG (Retrieval-Augmentation-Generation) approach** with embeddings and a local LLM to provide natural language responses with relevant employee recommendations.

---

## 2. Features
- Query employees by skills, experience, or projects (e.g., "Python + AWS developers").  
- Multi-skill filtering and advanced search.  
- Project-based employee suggestions.  
- AI-generated natural language responses.  
- Backend support with optional FastAPI endpoints.  
- Optional vector similarity search with embeddings for smarter retrieval.

---

## 3. Architecture
**System Components:**
1. **Frontend (Streamlit UI)** – Provides a user-friendly interface for queries.  
2. **RAG Component (`main.py`)**  
   - **Retrieval:** Finds employees based on query and embeddings.  
   - **Augmentation:** Combines employee data with query context.  
   - **Generation:** Uses a local LLM to generate readable responses.  
3. **Backend (`backend.py`)** – Optional helper functions and API endpoints.  
4. **Data Layer (`sample_data.json`)** – Stores employee information: skills, experience, projects, availability.  
5. **Deployment** – Hosted locally via Streamlit or on Streamlit Cloud.  

**Flow Diagram:**

User Query → Streamlit UI → RAG Chatbot → Employee Data → LLM Response → UI Display


---

## 4. Setup & Installation

# Step 1: Clone repository
git clone https://github.com/Sathyasri09/Hr_chatbot.git
cd rag_employee_chatbot

# Step 2: Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the Streamlit app
streamlit run app1.py


# 5. API Documentation
**Endpoints (optional FastAPI backend):
POST /chat
Description: Send a query to get employee recommendations.
Request Body:
{
    "query": "Find Python developers with 3+ years experience"
}
Response:
{
  "query": "2+ years as data analyst",
  "results": [
    {
      "name": "Maria Garcia",
      "experience_years": 5,
      "skills": ["Python", "SQL", "Power BI"],
      "projects": ["Sales Analytics", "Financial Dashboard"],
      "availability": "Currently busy"
    },
    {
      "name": "Emily Davis",
      "experience_years": 5,
      "skills": ["Data Science", "R", "Python"],
      "projects": ["Fraud Detection", "Customer Segmentation"],
      "availability": "Currently busy"
    },
    {
      "name": "John Miller",
      "experience_years": 6,
      "skills": ["C#", ".NET", "SQL Server"],
      "projects": ["ERP System", "Hospital Management Software"],
      "availability": "Currently busy"
    }
  ]
}
GET /employees/search?skill=Python

Description: Filter employees by skill or other parameters.


## 6. AI Development Process
Tools Used: ChatGPT, GitHub Copilot for code generation, debugging, and architecture planning.
AI Assistance:
Code generation: 40%
Debugging: 30%
Architecture decisions: 20%
Manual coding: 10% (integration, deployment)
Interesting AI solutions: Optimized data retrieval and response formatting.
Challenges solved manually: Integrating FAISS with local embeddings, customizing Streamlit UI for rich employee info.

# 7. Technical Decisions
RAG Approach: Combines semantic search with LLM-generated responses.
Local LLM vs Cloud API: Chose local HuggingFace + FAISS for cost savings and privacy.
Tech Stack: Streamlit (UI), Python (logic), FAISS (vector search), PyTorch/Transformers (LLM).
Trade-offs: Local compute requirements vs API cost and privacy.

# 8. Future Improvements
Multi-user authentication for HR access.
Real-time employee availability and scheduling.
Larger embedding datasets for better semantic search.
Deployment to scalable cloud infrastructure.

# 9. Demo
Local demo: Run streamlit run app1.py after setup.

Live demo (optional):https://hrchatbot-nvy5ttcrgvsr2zkxkgzxai.streamlit.app/

