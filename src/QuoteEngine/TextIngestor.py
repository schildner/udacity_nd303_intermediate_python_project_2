from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    ingestable_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        with open(path, 'r') as f:
            for line in f.readlines():
                body, author = line.split(' - ')
                new_quote = QuoteModel(body.strip(), author.strip())
                quotes.append(new_quote)

        return quotes
