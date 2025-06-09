from typing import List

from src.core.model.common import RawDocument, PreprocessedDocument
from src.infrastructure.database.mongo_client import MongoCustomClient


class Ingestor:

    def __init__(self):
        self.client = MongoCustomClient().client()

    @classmethod
    async def run(cls) -> List[PreprocessedDocument]:
        ingestor = cls()
        raw_documents = await ingestor.fetch()
        preprocessed_documents = await ingestor.preprocess(raw_documents)
        return preprocessed_documents

    async def fetch(self) -> List[RawDocument]:
        db = self.client["official_legal_data"]
        collection = db["legal_terms"]
        documents = collection.find({})

        raw_documents = []
        async for document in documents:
            raw_document = RawDocument(
                id=document['id'],
                _id=document['_id'],
                description=document['description'],
                term=document['term']
            )
            raw_documents.append(raw_document)
        return raw_documents

    async def preprocess(self, raw_documents: List[RawDocument]) -> List[PreprocessedDocument]:
        preprocessed_documents = []
        for raw_document in raw_documents:
            processed_text = self._clean_text(raw_document.description)
            combined_text = f"{raw_document.term}: {processed_text}"
            preprocessed_document = PreprocessedDocument(
                id=raw_document.id,
                text=combined_text,
                metadata={
                    "term": raw_document.term.strip(),
                    "document_type": "legal_term"
                }
            )
            preprocessed_documents.append(preprocessed_document)

        return preprocessed_documents

    def _clean_text(self, text: str) -> str:
        if not text:
            return ""

        cleaned = text.strip()
        cleaned = ' '.join(cleaned.split())
        return cleaned
