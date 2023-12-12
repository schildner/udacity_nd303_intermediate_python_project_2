# Udacity Nanodegree: Intermediate Python - Project 2: Meme Generator

## Project Overview

This project is part of the Udacity Nanodegree: Intermediate Python. The goal of this project is to create a meme generator using Python. The project is divided into two parts:

1. A command-line interface (CLI) tool that generates random memes.
2. A web application that generates memes on the web.

## Project Structure

The project is structured in the following way:

```bash
├── README.md
├── _data
│   ├── DogQuotes
│   │   ├── DogQuotesCSV.csv
│   │   ├── DogQuotesDOCX.docx
│   │   ├── DogQuotesPDF.pdf
│   │   └── DogQuotesTXT.txt
│   ├── photos
│   │   └── dog
│   │       ├── dog1.jpg
│   │       ├── dog2.jpg
│   │       ├── dog3.jpg
│   │       └── dog4.jpg
|   ├── SimpleLines
│   │   ├── SimpleLinesCSV.csv
│   │   ├── SimpleLinesDOCX.docx
│   │   ├── SimpleLinesPDF.pdf
│   │   └── SimpleLinesTXT.txt
│   └── templates
│       ├── base.html
│       ├── meme_form.html
│       └── meme.html
├── app.py
├── meme.py
├── requirements.txt
└── .gitignore
```

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
python3 app.py
```

Then, you can access the web application on your browser at the following address: http://

## Acknowledgments

* Starter code: [Udacity](https://www.udacity.com/) - see the initial commit on main branch.
