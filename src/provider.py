from __future__ import annotations
from abc import ABC, abstractmethod
import os
import yaml


class LLMProvider(ABC):
    @abstractmethod
    def complete(self, system: str, user: str, **kw) -> str:
        ...


class OllamaProvider(LLMProvider):
    def __init__(self, model: str):
        import ollama
        self._ollama = ollama
        self.model = model

    def complete(self, system: str, user: str, **kw) -> str:
        resp = self._ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resp["message"]["content"]


class AzureProvider(LLMProvider):
    def __init__(self, deployment: str | None):
        if not deployment:
            raise RuntimeError(
                "Azure provider selected but not configured yet. "
                "Fill in .env and configs/default.yaml, or use provider: local."
            )
        # Real Azure OpenAI client wiring comes when we do that milestone.
        self.deployment = deployment

    def complete(self, system: str, user: str, **kw) -> str:
        raise NotImplementedError("Azure provider not wired up yet.")


def load_config(path: str = "configs/default.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def get_provider(cfg: dict | None = None) -> LLMProvider:
    cfg = cfg or load_config()
    name = cfg["provider"]
    if name == "local":
        return OllamaProvider(model=cfg["local"]["model"])
    elif name == "azure":
        return AzureProvider(deployment=cfg["azure"]["deployment"])
    raise ValueError(f"Unknown provider: {name}")
