import os
import replicate
from ..llm_wrapper import BaseLLM

class ReplicateAPI_LLM(BaseLLM):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.api_token = os.environ.get("REPLICATE_API_TOKEN")
        replicate.Client(api_token=self.api_token)

    def generate(self, prompt: str, **kwargs) -> str:
        output = replicate.run(
            self.model_name,
            input={"prompt": prompt, **kwargs}
        )
        return output
