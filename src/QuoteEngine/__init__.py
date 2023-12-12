"""
The QuoteEngine package provides functionality for ingesting and processing quotes from various file formats.

Modules:
- Ingestor: A class for ingesting quotes from different file formats.
- IngestorInterface: An interface for the Ingestor class.
- QuoteModel: A class representing a quote.

Ingestor Modules:
- CSVIngestor: A class for ingesting quotes from CSV files.
- DocxIngestor: A class for ingesting quotes from DOCX files.
- PDFIngestor: A class for ingesting quotes from PDF files.
- TextIngestor: A class for ingesting quotes from plain text files.
"""

from .Ingestor import Ingestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
