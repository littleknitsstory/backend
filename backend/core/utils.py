from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark_text(input_image_path, output_image_path, text, pos):
    """
    It print the text right on the input image
    :param input_image_path:
    :param output_image_path:
    :param text:
    :param pos: it should contain of a tuple with X and Y positions.
    Example: (0,0) is a top left corner of the image
    :return:
    """
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (200, 200, 200)  # font color
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(
        pos, text,
        fill=black,
        font=font
    )
    photo.show()
    photo.save(output_image_path)


