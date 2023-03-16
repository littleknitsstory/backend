import shutil

IMAGE_EXTENSIONS = ("jpg", "jpeg", "png", "bmp")


def check_extension(file: str) -> bool:
    """Check file extension"""
    extension: str = file.split(".")[-1].lower()
    if extension not in IMAGE_EXTENSIONS:
        return False
    return True


def copy_image_to_media_folder(image_preview: str, folder: str):
    """Copy file"""
    if check_extension(image_preview):
        filename = image_preview.split("/")[-1]
        image_path = f"articles/{filename}"

        shutil.copy(image_preview, folder)
        return image_path
