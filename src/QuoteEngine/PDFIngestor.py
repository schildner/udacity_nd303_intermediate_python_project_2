import os
import subprocess
import random
import re

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    ingestable_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the PDF file at the given path and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                # Two groups: quote and author
                # quote is in double quotes - extracting without quotes
                # author is one or more words
                regex_pattern = r'"(.*?)"\s*-\s*(\w+\s*\w*)'
                tuples = re.findall(regex_pattern, line)
                for quote, author in tuples:
                    new_quote = QuoteModel(quote.strip(), author.strip())
                    quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
