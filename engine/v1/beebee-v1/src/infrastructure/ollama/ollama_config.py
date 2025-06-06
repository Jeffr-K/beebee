import os

from attr import dataclass


@dataclass
class OllamaConfig:
    ollama_host: str = os.getenv("OLLAMA_HOST")
    ollama_port: int = int(os.getenv("OLLAMA_PORT"))
    ollama_embedding_model: str = os.getenv("OLLAMA_EMBEDDING_MODEL")
    timeout: int = 30

    @property
    def base_url(self) -> str:
        return f"http://{self.ollama_host}:{self.ollama_port}"

    @property
    def host(self) -> str:
        return self.ollama_host

    @property
    def port(self) -> int:
        return self.ollama_port
