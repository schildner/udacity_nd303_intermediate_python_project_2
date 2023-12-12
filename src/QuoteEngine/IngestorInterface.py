from typing import List
from abc import ABC, abstractmethod

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    ingestable_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension = path.split('.')[-1]
        return file_extension in cls.ingestable_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
