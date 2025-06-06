from src.core.chains.embedder.embedder import Embedder
from src.core.chains.ingestor.ingestor import Ingestor
from src.core.chains.search.search import Search


class Pipeline:
    def __init__(self):
        self.ingestor = Ingestor()
        self.embedder = Embedder()


    @classmethod
    async def run(cls):
        pipeline = cls()

        collection_setup = await pipeline.embedder.setup_collection()
        if not collection_setup:
            print("Collection setup failed")
            return False

        preprocessed_documents = await pipeline.ingestor.run()
        embedding_success = await pipeline.embedder.store(preprocessed_documents)

        if embedding_success:
            print("Pipeline completed successfully!")
            return True
        else:
            print("Embedding storage failed")
            return False

    # @classmethod
    # async def search(cls, query: str, limit: int = 5):
    #     pipeline = cls()
    #     return await pipeline.embedder.search(query, limit)

    @classmethod
    async def search(cls, query: str):
        search = Search()
        return await search.answer(query)