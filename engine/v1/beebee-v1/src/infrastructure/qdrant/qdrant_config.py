import os
from qdrant_client import QdrantClient
from typing import Optional


class QdrantConfig:
    @classmethod
    def connect(cls) -> dict:
        return {
            "url": os.getenv("QDRANT_URL", "http://localhost:6333"),
            "api_key": os.getenv("QDRANT_API_KEY"),
            "timeout": 60,
            "prefer_grpc": False
        }


class QdrantCustomClient:
    _client: Optional[QdrantClient] = None

    @classmethod
    def client(cls) -> QdrantClient:
        if cls._client is None:
            config = QdrantConfig.connect()

            client_kwargs = {
                "url": config["url"],
                "timeout": config["timeout"],
                "prefer_grpc": config["prefer_grpc"]
            }

            if config["api_key"] is not None:
                client_kwargs["api_key"] = config["api_key"]

            cls._client = QdrantClient(**client_kwargs)
            print("Qdrant client created successfully.")

        return cls._client

    @classmethod
    def close(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            print("Qdrant client closed.")