from motor.motor_asyncio import AsyncIOMotorClient

from src.infrastructure.database.mongo_config import MongoDBConfig


class MongoCustomClient:
    def __init__(self):
        self._client: AsyncIOMotorClient = MongoDBConfig.connect()

    def client(self) -> AsyncIOMotorClient:
        return self._client
