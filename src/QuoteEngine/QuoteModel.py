class QuoteModel():
    """Represents a quote with a body and an author."""

    def __init__(self, body: str, author: str):
        """
        Initialize a QuoteModel object.

        Args:
            body (str): The body of the quote.
            author (str): The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """
        Return a string representation of the QuoteModel object.

        The body of the quote and the author formatting are defined
        in the project's specification.

        Return:
            str: A string representation of QuoteModel.
        """
        return f'"{self.body}" - {self.author}'
