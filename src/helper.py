import base64
import io
from pdf2image import convert_from_bytes


def image_to_base64_img(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_base64


def pdf_to_base64_img(pdf_uploaded):
    images = convert_from_bytes(pdf_uploaded.read())
    # TODO: get only the first page for now
    img = images[0] 
    
    return image_to_base64_img(img)