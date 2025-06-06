import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()


class MongoDBConfig:
    _client: AsyncIOMotorClient | None = None

    @classmethod
    def connect(cls) -> AsyncIOMotorClient:
        if cls._client is not None:
            return cls._client

        server_selection_timeout_ms = int(os.getenv("MONGO_SERVER_SELECTION_TIMEOUT_MS", 5000))

        uri = os.getenv("MONGO_URI")

        if uri is None:
            raise ValueError("No value in MONGO_URI environment variable.")
        try:
            cls._client = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=server_selection_timeout_ms)
            print("MongoDB client created successfully.")
            return cls._client
        except Exception as e:
            print(f"Failed to create MongoDB client: {e}")
            raise RuntimeError("Cannot create MongoDB client") from e

    @classmethod
    async def ping(cls) -> bool:
        try:
            client = cls.connect()
            await client.admin.command("ping")
            print("Successfully connected to MongoDB.")
            return True
        except Exception as e:
            print(f"Failed to ping MongoDB: {e}")
            return False
