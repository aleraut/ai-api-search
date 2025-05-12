from src.parser import extract_endpoints
from src.gpt_integration import ask_gpt

def create_context(endpoints):
    context = ""
    for ep in endpoints:
        context += f"{ep['method']} {ep['path']}: {ep['description']}\n"
    return context

def search_api(swagger_data, user_question):
    endpoints = extract_endpoints(swagger_data)
    context = create_context(endpoints)
    prompt = f"Tässä on API-dokumentaatio:\n{context}\n\nKäyttäjän kysymys: {user_question}\n\nMikä endpointti liittyy tähän kysymykseen?"
    return ask_gpt(prompt)
