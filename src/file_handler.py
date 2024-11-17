import base64
import io
from PIL import Image
from pdf2image import convert_from_bytes


class FileHandler:
    """
    A utility class for handling file processing tasks.
    Provides static methods to process PDFs and images into base64-encoded images.
    """

    @staticmethod
    def image_to_base64_img(img):
        """
        Convert an image object into a base64-encoded PNG image string.
        """
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

    @staticmethod
    def pdf_to_base64_img(pdf):
        """
        Convert the first page of a PDF into a base64-encoded PNG image string.
        """
        images = convert_from_bytes(pdf.read())
        img = images[0]  # TODO: Process only the first page for now
        return FileHandler.image_to_base64_img(img)

    @staticmethod
    def process_uploaded_file(uploaded_file):
        """
        Process the uploaded file and convert it into a base64-encoded image.
        Supports both PDF and image file formats.
        """
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            return FileHandler.pdf_to_base64_img(uploaded_file)
        else:
            return FileHandler.image_to_base64_img(Image.open(uploaded_file))
