from __future__ import annotations
from abc import ABC, abstractmethod
import os
import yaml
from dotenv import load_dotenv

load_dotenv()


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
    def __init__(self, endpoint: str | None, api_key: str | None, deployment: str | None):
        if not (endpoint and api_key and deployment):
            raise RuntimeError(
                "Azure provider selected but not fully configured. "
                "Check AZURE_OPENAI_ENDPOINT / AZURE_OPENAI_API_KEY in .env, "
                "and azure.deployment in configs/default.yaml."
            )
        from openai import OpenAI

        self._client = OpenAI(
            base_url=endpoint,
            api_key=api_key,
        )
        self.deployment = deployment

    def complete(self, system: str, user: str, **kw) -> str:
        resp = self._client.chat.completions.create(
            model=self.deployment,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resp.choices[0].message.content


def load_config(path: str = "configs/default.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def get_provider(cfg: dict | None = None) -> LLMProvider:
    cfg = cfg or load_config()
    name = cfg["provider"]

    if name == "local":
        return OllamaProvider(model=cfg["local"]["model"])
    elif name == "azure":
        return AzureProvider(
            endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
            deployment=cfg["azure"]["deployment"],
        )
    raise ValueError(f"Unknown provider: {name}")