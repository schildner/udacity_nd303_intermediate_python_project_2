from QuoteEngine import Ingestor

print('Testing Ingestor.parse()')
print('CSV...')
print(Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
print('Docx...')
print(Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
print('PDF...')
print(Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
print('TXT...')
print(Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
