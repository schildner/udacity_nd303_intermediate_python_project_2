class QuoteModel():

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        print(f'"{self.body}" - {self.author}')
