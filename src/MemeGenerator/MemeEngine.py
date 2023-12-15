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

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme image with specified width and including text & author.

        Args:
            str -- the file path to the output image.
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
            draw.text((10, 100), author, font=font_author, fill='yellow')

        print(f"Saving meme to {self.output_dir}")
        meme_path = f'./{self.output_dir}/{randint(0,1000000)}.jpg'
        img.save(meme_path)
        return meme_path
