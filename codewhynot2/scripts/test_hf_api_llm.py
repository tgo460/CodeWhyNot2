from dotenv import load_dotenv
load_dotenv()

from src.models.implementations.hf_api import HuggingFaceAPI_LLM

model_name = "gpt2"  # This model is available for API inference

llm = HuggingFaceAPI_LLM(model_name=model_name)

prompt = (
    "Write a Python function called add_numbers that takes two numbers and returns their sum. "
    "Only output valid Python code. The function should have a docstring that describes its purpose and parameters. "
    "Use clear and descriptive variable names and follow PEP 8 style guidelines. "
    "The function should handle input errors, such as non-numeric inputs, and return an appropriate error message. "
    "Test the function with multiple input values to ensure it works correctly."
)

try:
    result = llm.generate(prompt)
    print("=== LLM Python Code Output ===\n")
    print(result)
except Exception as e:
    print(f"Error: {e}")