# Udacity Nanodegree: Intermediate Python - Project 2: Meme Generator

## Project Overview

This project is part of the Udacity Nanodegree: Intermediate Python. The goal of this project is to create a meme generator using Python. The project is divided into two parts:

1. A command-line interface (CLI) tool that generates random memes.
2. A web application that generates memes on the web.

## Project Structure

The project has the following structure:

- `app.py`: Main entry point of our application. It sets up our Flask application and routes.
- `meme.py`: This module is responsible for generating memes.
- `requirements.txt`: List of Python (sub-)dependencies the project needs in order to run.
- `.gitignore`: This file tells git which files it should ignore.

The `templates` directory contains HTML templates for the Flask application:

- `base.html`: This is the base template that other templates extend.
- `meme_form.html`: This template contains a form that users can use to create a meme.
- `meme.html`: This template displays a generated meme.

### Python Modules

- `MemeGenerator`: This module is responsible for generating memes. It takes an image path, a quote body, and a quote author as input, draws the quote text onto the image, and saves the result.

    Example usage:

    ```python
    from MemeGenerator import MemeGenerator

    meme = MemeGenerator('output_path')
    meme.make_meme('input_image.jpg', 'quote text', 'quote author')
    ```

- `QuoteEngine`: This module is responsible for loading quotes from a variety of file types. It includes a `QuoteModel` class for representing quotes and an `Ingestor` class for loading quotes.

    Example usage:

    ```python
    from QuoteEngine import Ingestor, QuoteModel

    quotes = Ingestor.parse('quotes.csv')
    quote = QuoteModel('quote body', 'quote author')
    ```

## Dependencies

This project uses the following dependencies:

- Flask: A lightweight web application framework.
- Pillow: A Python Imaging Library used for opening, manipulating, and saving images.

## Installation

To install the project, you need to clone the repository and install the dependencies:

```bash
git clone
cd project_meme_generator
pip install -r requirements.txt
```

## Usage

### CLI Tool

To use the CLI tool, you need to run the following command:

```bash
python3 meme.py
```

The CLI tool has the following arguments:

```bash
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      Path to an image file
  --body BODY      Quote body to add to the image
  --author AUTHOR  Quote author to add to the image
```

### Web Application

To use the web application, you need to run the following command:

```bash
FLASK_APP=app.py
flask run
```

This will start a Flask development server. A meme can be created by navigating to [http://localhost:5000/](http://localhost:5000) in a web browser and filling out the form.

## Acknowledgments

- Starter code: [Udacity](https://www.udacity.com/) - see the initial commit on main branch.
