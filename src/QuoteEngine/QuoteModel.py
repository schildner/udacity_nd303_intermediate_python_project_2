class QuoteModel():

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'"{self.body}" - {self.author}'
