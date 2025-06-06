from dataclasses import dataclass

from bson import ObjectId

@dataclass
class RawDocument:
    id: int
    _id: ObjectId
    description: str
    term: str


@dataclass
class PreprocessedDocument:
    id: int
    text: str
    metadata: dict