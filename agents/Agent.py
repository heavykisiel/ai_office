import random
from transformers import pipeline
from huggingface_hub import InferenceClient
import requests

class Agent:
    def __init__(self, name, api_token, role="Brainstormer"):
        """
        Initialize an agent with a name, model, and role.
        :param name: Name of the agent.
        :param role: The role of the agent (e.g., Brainstormer, Evaluator).
        """
        self.name = name
        self.role = role
        self.model = "Qwen2.5-72B-Instruct "
        self.personality = self._set_personality()
        self.history = []  # Stores the agent's contributiionis
        self.api_token = api_token

    def _set_personality(self):
        """Assign a random personality trait for creativity."""
        personalities = [
            "creative thinker",
            "practical strategist",
            "visionary",
            "critical evaluator",
        ]
        return random.choice(personalities)
    def _get_model_pipeline(self):

        headers = {"Authorization": f"Bearer {self.api_token}"}
        url = f"https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
        # Example of sending a request to Hugging Face API
        def model_pipeline(prompt, **kwargs):
            response = requests.post(url, headers=headers, json={"inputs": prompt, **kwargs})
            if response.status_code == 200:
                return response.json()[0].get('generated_text', '')
            else:
                raise Exception(f"Error fetching model: {response.status_code} - {response.text}")
    
        return model_pipeline
    def generate_idea(self, prompt):

        model_pipeline = self._get_model_pipeline()
        return model_pipeline(prompt, max_length=300, num_return_sequences=1)
