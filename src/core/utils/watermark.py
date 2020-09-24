# TODO: reprite this place and implemented solved
# from PIL import Image, ImageDraw, ImageFont
# from settings.components.watermark import WATERMARK_TEXT, \
#     WATERMARK_POSITION, IMAGE_SIZE, WATERMARK_FONT
# from settings.components.watermark import WATERMARK_TEXT, WATERMARK_POSITION, WATERMARK_FONT, IMAGE_SIZE


# def watermark_text(input_image_path, output_image_path, text=WATERMARK_TEXT,
#                    pos=WATERMARK_POSITION, font=WATERMARK_FONT):
#     """
#     It print the text right on the input image
#     :param font: path in settings
#     :param input_image_path:
#     :param output_image_path:
#     :param text:
#     :param pos: it should contain of a tuple with X and Y positions.
#     Example: (0,0) is a top left corner of the image
#     :return:
#     """
#     photo = Image.open(input_image_path)
#     resizing
# photo.thumbnail(IMAGE_SIZE, Image.ANTIALIAS)
#
# make the image editable
# drawing = ImageDraw.Draw(photo)
#
# font_color = (200, 200, 200)
# font = ImageFont.truetype(font, 40)
# drawing.text(
#     pos, text,
#     fill=font_color,
#     font=font
# )
# photo.show()  # just to show the result picture when you test it
# photo.save(output_image_path)
#
