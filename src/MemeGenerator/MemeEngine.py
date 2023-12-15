"""This module provides a MemeEngine class for generating memes."""

import os
from random import randint
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """A meme generator."""

    def __init__(self, output_dir='static'):
        """
        Initialize the MemeEngine object.

        Args:
            output_dir (str): Directory to save the generated memes. Defaults to 'static'.
        """
        self.output_dir = output_dir

    def save(self, img, path) -> None:
        """Save the meme image in the path directory and return the new image path."""
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as e:
                print(e)

        try:
            img.save(path)
        except PermissionError as e:
            print(f"Unable to save image as write access was denied for {path}: {e}")
        except FileNotFoundError as e:
            print(f"Unable to save image as target directory doesnt exist {path}: {e}")
        except OSError as e:
            print(f"Unable to save image at {path}: {e}")

        return path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme image with specified width and including text & author.

        Args:
            img_path (str): The file path to the input image.
            text (str): The text to be added to the meme image.
            author (str): The author to be added to the meme image.
            width (int): The width of the meme image. Defaults to 500.

        Returns:
            str: The file path to the generated meme image.
        """
        img = Image.open(img_path)
        original_width, original_height = img.size

        if width > 500:
            width = 500

        # New height must respect the aspect ratio of the original image.
        new_height = int(width * original_height / original_width)
        img = img.crop((0, 0, width, new_height))

        draw = ImageDraw.Draw(img)
        font_file_path = './MemeGenerator/.fonts/LilitaOne-Regular.ttf'
        font_text = ImageFont.truetype(font_file_path, size=40)
        font_author = ImageFont.truetype(font_file_path, size=20)

        if text is not None:
            draw.text((10, 30), text, font=font_text, fill='white')

        if author is not None:
            # Add author text to the meme image
            draw.text((10, 100), author, font=font_author, fill='yellow')

        print(f"Saving meme to {self.output_dir}")
        target_path = f'./{self.output_dir}/{randint(0,1000000)}.jpg'
        meme_path = self.save(img, target_path)
        return meme_path
