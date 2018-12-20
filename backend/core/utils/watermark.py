from PIL import Image, ImageDraw, ImageFont


WATERMARK_TEXT = "\u00A9 Little Knits Story"
WATERMARK_POSITION = (5, 5)  # x, y


def watermark_text(input_image_path, output_image_path, text=WATERMARK_TEXT, pos=WATERMARK_POSITION):
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

    font_color = (200, 200, 200)  # font color
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(
        pos, text,
        fill=font_color,
        font=font
    )
    # photo.show()  # just to show the result picture when you test it
    photo.save(output_image_path)


