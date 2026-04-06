from google import genai
import os, json
from dotenv import load_dotenv
load_dotenv()

class BaseAgent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction=system_prompt
        )

    def run(self, message) -> dict:
        try:
            response = self.model.generate_content(message)
            text = response.text.strip()
            # Strip markdown fences if present
            text = text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except Exception as e:
            # Safe fallback if parsing fails
            return {
                "signal": "HOLD",
                "confidence": 50,
                "reasoning": f"Agent error: {str(e)}"
            }