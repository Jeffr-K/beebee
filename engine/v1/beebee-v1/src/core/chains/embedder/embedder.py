from typing import List
from sentence_transformers import SentenceTransformer
from qdrant_client.models import Distance, VectorParams, PointStruct

from src.infrastructure.qdrant.qdrant_config import QdrantCustomClient
from src.core.model.common import PreprocessedDocument


class Embedder:

    def __init__(self, collection_name: str = "legal_terms", model_name: str = "jhgan/ko-sroberta-multitask"):
        self.client = QdrantCustomClient.client()
        self.collection_name = collection_name
        self.model = SentenceTransformer(model_name)
        self.embedding_dim = self.model.get_sentence_embedding_dimension()

    async def setup_collection(self) -> bool:
        try:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.embedding_dim,
                    distance=Distance.COSINE
                )
            )
            return True
        except Exception as e:
            print(f"Collection setup error: {e}")
            return False

    async def embed(self, text: str) -> List[float]:
        embedding = self.model.encode(text)
        return embedding.tolist()

    async def store(self, documents: List[PreprocessedDocument]) -> bool:
        try:
            points = []
            for i, document in enumerate(documents):
                embedding = await self.embed(document.text)
                point = PointStruct(
                    id=i,
                    vector=embedding,
                    payload={
                        "id": document.id,
                        "text": document.text,
                        "metadata": document.metadata
                    }
                )
                points.append(point)
            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            print(f"{len(points)}: stored successfully.")
            return True
        except Exception as e:
            print(f"failed to store. {e}")
            return False

    async def search(self, query: str, limit: int = 5, score_threshold: float = 0.7) -> List[dict]:
        try:
            query_embedding = await self.embed(query)
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                score_threshold=score_threshold
            )
            results = []
            for result in search_results:
                results.append({
                    "score": result.score,
                    "text": result.payload.get("text"),
                    "metadata": result.payload.get("metadata", {})
                })

            return results

        except Exception as e:
            print(f"❌ 검색 실패: {e}")
            return []