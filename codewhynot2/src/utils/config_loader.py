from pydantic import BaseModel
from typing import Optional

class LLMConfig(BaseModel):
    type: str
    model_name: str
    device: Optional[str] = None

    model_config = {'protected_namespaces': ()}
