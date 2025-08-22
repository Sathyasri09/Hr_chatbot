from sentence_transformers import SentenceTransformer, util

class RAGChatbot:
    def __init__(self, employees):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.employees = employees

    def employee_to_text(self, emp):
        return f"{emp['name']} | Skills: {', '.join(emp['skills'])} | {emp['experience_years']} yrs exp | Projects: {', '.join(emp['projects'])} | Availability: {emp['availability']}"

    def search(self, query, top_k=3):
        query_emb = self.model.encode(query, convert_to_tensor=True)
        scored = []
        for emp in self.employees:
            emp_text = self.employee_to_text(emp)
            emp_emb = self.model.encode(emp_text, convert_to_tensor=True)
            score = util.cos_sim(query_emb, emp_emb).item()
            scored.append((emp, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [emp for emp, _ in scored[:top_k]]

    def generate_response(self, query):
        candidates = self.search(query)
        if not candidates:
            return "Sorry, I couldn’t find any matching employees."

        response = f"Based on your query: *{query}*, I recommend:\n\n"
        for emp in candidates:
            response += f"**{emp['name']}** – {emp['experience_years']} years exp, skills in {', '.join(emp['skills'])}, worked on {', '.join(emp['projects'])}. Currently {emp['availability']}.\n\n"
        return response
