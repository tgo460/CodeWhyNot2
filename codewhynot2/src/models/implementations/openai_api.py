from codewhynot2.src.models.llm_wrapper import BaseLLM


class OpenAI_API_LLM(BaseLLM):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate(self, prompt: str, **kwargs) -> str:
        ...
