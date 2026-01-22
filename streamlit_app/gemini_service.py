import os
import google.generativeai as genai
from data import KNOWLEDGE_BASE

SYSTEM_INSTRUCTION_BASE = """
You are Aeronix, a world-class AI assistant specialized in Airport Ground Operations. 
Your goal is to provide clear, helpful, and reassuring explanations about airport processes.

STRICT RULES:
1. DO NOT issue boarding passes or modify flight details.
2. DO NOT provide specific live flight status (gates/times) unless it's in the provided context.
3. Keep answers concise and structured using bullet points.
4. If asked for something out of scope, politely redirect to the helpdesk.
5. Provide "Pro-tips" relevant to the passenger's situation.
"""

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY") 
        if not api_key:
            # Fallback or error handling
            print("Warning: GEMINI_API_KEY not found in environment variables.")
        
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp') # Using flash model as in original

    def get_relevant_context(self, query: str) -> str:
        # Improved Strategy: Provide FULL context for better quality. 
        # The dataset is small enough to fit in the context window.
        
        # 1. Knowledge Base
        kb_text = "\n".join([f"- {entry.content}" for entry in KNOWLEDGE_BASE])
        
        # 2. Terminal Zones Status (Real-time context)
        # We need to access the zones. Since we are in the service, we can import the default English ones or just raw data.
        # Ideally, we pass the current state, but reading from constants is fine for this scope.
        from .data import TERMINAL_ZONES # This is now the default English list from our previous edit
        zones_text = "\n".join([f"- {z.name}: Status {z.status}, Wait {z.waitTime} mins. ({z.description})" for z in TERMINAL_ZONES])
        
        return f"""
\n\nRELEVANT AIRPORT KNOWLEDGE BASE:
{kb_text}

LIVE TERMINAL STATUS:
{zones_text}
"""

    def send_message(self, message: str, history: list, language: str = 'en', passenger_type: str = 'standard'):
        try:
            local_context = self.get_relevant_context(message)
            language_instruction = f"Respond ONLY in the following language code: {language}."
            passenger_instruction = f"The user is a {passenger_type} passenger. Tailor your advice to their needs."
            
            full_system_instruction = f"{SYSTEM_INSTRUCTION_BASE}\n{language_instruction}\n{passenger_instruction}\n{local_context}"
            
            # Create a new chat session with system instruction (simulated by prepending to history or config if supported)
            # The python SDK supports system_instruction in GenerativeModel constructor or generate_content.
            # However, for chat sessions, it's best to set it on model instantiation or send as first part.
            # We'll use a fresh model/chat for simplicity each turn or maintain a chat session object in state.
            
            # Ideally, we maintain a `chat` object in Streamlit session state. 
            # But the service method here is stateless in the React version (it sends full history).
            # We will replicate the stateless behavior for now.
            
            chat_history = []
            for h in history:
                role = 'model' if h['role'] == 'assistant' else 'user'
                chat_history.append({'role': role, 'parts': [h['content']]})

            # We use `generate_content` instead of `start_chat` to easily inject system prompt each time if needed,
            # but `start_chat` is better for history. 
            # Let's instantiate a model with system_instruction for this request.
            
            model = genai.GenerativeModel(
                'gemini-2.0-flash-exp',
                system_instruction=full_system_instruction
            )
            
            response = model.generate_content([
                *chat_history,
                {'role': 'user', 'parts': [message]}
            ])
            
            return response.text
            
        except Exception as e:
            print(f"Gemini API Error: {e}")
            return "I'm having trouble connecting to my brain. Please try again in a moment."

gemini_service = GeminiService()
