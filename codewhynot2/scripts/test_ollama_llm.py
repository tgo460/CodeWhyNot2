from src.models.implementations.ollama_local import OllamaLLM
import os

# Set the correct port for Ollama (update if needed)
ollama_port = os.environ.get("OLLAMA_PORT", "11434")  # Default to 50147 if not set
ollama_base_url = f"http://localhost:{ollama_port}"

# Use the phi3 model
llm = OllamaLLM(model_name="phi3", base_url=ollama_base_url)

prompt = ("Write a Python function called add_numbers that takes two numbers and returns their sum. ")

print("Prompt:", prompt)
result = llm.generate(prompt)
print("Result:", result)
print("=== LLM Python Code Output ===\n")
print(result)
