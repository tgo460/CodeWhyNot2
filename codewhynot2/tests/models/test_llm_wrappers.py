import pytest
from src.models.llm_wrapper import get_llm
from src.utils.config_loader import LLMConfig

# Example test for HuggingFaceAPI_LLM (mocked)
def test_hf_api_llm(monkeypatch):
    class DummyResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return [{"generated_text": "def foo(): pass"}]
    def dummy_post(*args, **kwargs):
        return DummyResponse()
    import src.models.implementations.hf_api as hf_api
    monkeypatch.setattr(hf_api.requests, "post", dummy_post)
    config = LLMConfig(type="huggingface_api", model_name="dummy-model")
    llm = get_llm(config)
    result = llm.generate("Write a function")
    assert "def foo" in result
