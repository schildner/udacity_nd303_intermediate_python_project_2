import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Ingestor for Docx files."""
    ingestable_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the Docx file at the given path and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                # Remove the quotes from the text
                line = para.text.replace('\"', '')
                quote, author = line.split(' - ')
                new_quote = QuoteModel(quote.strip(), author.strip())
                quotes.append(new_quote)

        return quotes
