import requests
import os
from ..llm_wrapper import BaseLLM

API_URL = "https://api-inference.huggingface.co/models/"
HF_API_TOKEN = os.environ.get("HF_API_TOKEN")

class HuggingFaceAPI_LLM(BaseLLM):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

    def generate(self, prompt: str, **kwargs) -> str:
        response = requests.post(
            API_URL + self.model_name,
            headers=self.headers,
            json={"inputs": prompt, "parameters": kwargs}
        )
        response.raise_for_status()
        return response.json()[0]['generated_text']
