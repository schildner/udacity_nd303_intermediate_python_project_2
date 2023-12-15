
"""
This module contains the Flask application for a meme generator.

It includes routes for generating random memes and creating user-defined memes.
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the quote_files variable
    quotes = []
    for quote_file in quote_files:
        quotes_from_file = Ingestor.parse(quote_file)
        for quote in quotes_from_file:
            quotes.append(quote)

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for file in os.listdir(images_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)

    print(f"Source image: {img}")
    print(f"Quote: {quote}")

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form.get('image_url')
    quote_text = request.form.get('body')
    quote_author = request.form.get('author')

    print(f"Source image: {image_url}, Quote: {quote_text}, {quote_author}")

    image_name = os.path.basename(image_url)
    tmp_src_image = os.path.join('tmp', image_name)
    download_image(image_url, tmp_src_image)

    path = meme.make_meme(tmp_src_image, quote_text, quote_author)
    os.remove(tmp_src_image)

    return render_template('meme.html', path=path)


def download_image(url, save_path):
    """Download image from url and save to save_path."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully: {save_path}.")
    else:
        print(f"Failed to download image: {url}.")


if __name__ == "__main__":
    app.run()
