import requests
from ..llm_wrapper import BaseLLM
import os

class OllamaLLM(BaseLLM):
    def __init__(self, model_name: str = "qwen3:4b", base_url: str = None):
        # Always use the default REST API port 11434 for Ollama
        # Make sure to start the server with: ollama serve
        if base_url is None:
            base_url = "http://localhost:11434"
        self.model_name = model_name
        self.base_url = base_url

    def generate(self, prompt: str, **kwargs) -> str:
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": self.model_name, "prompt": prompt, "stream": False},
                timeout=60
            )
            response.raise_for_status()
            data = response.json()
            print("Ollama API raw response:", data)  # Debug print
            return data.get("response", "")
        except requests.exceptions.ConnectionError:
            print(f"Could not connect to Ollama server at {self.base_url}. Is it running on this port? (Tip: Use 'ollama serve')")
            return ""
        except Exception as e:
            print("Ollama API error:", e)
            return ""
