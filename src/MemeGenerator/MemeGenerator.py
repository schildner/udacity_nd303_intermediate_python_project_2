from random import randint
from PIL import Image


def make_meme(self, img_path, text, author, width=500) -> str:
    """Create a meme image with specified width and including text & author.

        str -- the file path to the output image.
    """
    img = Image.open(img_path)
    original_width, original_height = img.size

    if width > 500:
        width = 500

    # New height must respect the aspect ratio of the original image.
    new_height = int(width * original_height / original_width)
    img = img.crop((0, 0, width, new_height))

    img = img.crop((0, 0, width, new_height))

    meme_path = f'./memes/{randint(0,1000000)}.jpg'
    img.save(meme_path)
    return meme_path
