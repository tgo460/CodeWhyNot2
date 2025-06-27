from abc import ABC, abstractmethod
from ..utils.config_loader import LLMConfig

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass

def get_llm(config: LLMConfig) -> BaseLLM:
    """Factory function to get the correct LLM wrapper based on config."""
    if config.type == "huggingface_api":
        from .implementations import hf_api
        return hf_api.HuggingFaceAPI_LLM(model_name=config.model_name)
    elif config.type == "replicate_api":
        from .implementations import replicate_api
        return replicate_api.ReplicateAPI_LLM(model_name=config.model_name)
    elif config.type == "local":
        from .implementations import hf_local
        return hf_local.HuggingFaceLocalLLM(model_name=config.model_name)
    elif config.type == "ollama_local":
        from .implementations import ollama_local
        return ollama_local.OllamaLLM(model_name=config.model_name)
    else:
        raise ValueError(f"Unknown LLM type in config: {config.type}")
