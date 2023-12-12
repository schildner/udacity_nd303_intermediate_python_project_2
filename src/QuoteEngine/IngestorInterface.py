from typing import List
from abc import ABC, abstractmethod

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    An abstract base class for ingesting different types of files and extracting quotes.

    Attributes:
        ingestable_extensions (List[str]): File extensions that can be ingested.

    Methods:
        can_ingest(path: str) -> bool: Check if a file with the given path can be ingested.
        parse(path: str) -> List[QuoteModel]: Parse a file with the given path and QuoteModel objects.
    """

    ingestable_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if a file with the given path can be ingested.

        Args:
            path (str): The path of the file to check.

        Return:
            bool: True if the file can be ingested, False otherwise.
        """
        file_extension = path.split('.')[-1]
        return file_extension in cls.ingestable_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a file with the given path and returns a list of QuoteModel objects.

        Args:
            path (str): The path of the file to parse.

        Return:
            List[QuoteModel]: A list of QuoteModel objects extracted from the file.
        """
        pass
