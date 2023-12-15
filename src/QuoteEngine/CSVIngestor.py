"""This module defines the CSVIngestor class."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingestor for CSV files."""

    ingestable_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the CSV file at the given path and return a list of QuoteModel objects.

        Args:
            path (str): The path to the CSV file.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the CSV file.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        df = pd.read_csv(path, header=0)
        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        return quotes
