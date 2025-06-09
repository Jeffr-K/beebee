from src.infrastructure.database.mongo_config import MongoDBConfig


class Bootstrap:
    @classmethod
    def dependencies(cls):
        MongoDBConfig().connect()
