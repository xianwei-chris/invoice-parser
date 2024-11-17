from unittest.mock import Mock, patch
from PIL import Image

from file_handler import FileHandler


def test_image_to_base64_img():
    # Create a dummy image
    img = Image.new("RGB", (100, 100), color="red")
    result = FileHandler.image_to_base64_img(img)

    # Assert result is a base64 string
    assert isinstance(result, str)
    assert len(result) > 0


@patch("file_handler.convert_from_bytes")
def test_pdf_to_base64_img(mock_convert_from_bytes):
    # Mock PDF and conversion
    mock_pdf = Mock()
    mock_pdf.read.return_value = b"dummy_pdf_content"
    mock_image = Image.new("RGB", (100, 100), color="blue")
    mock_convert_from_bytes.return_value = [mock_image]

    result = FileHandler.pdf_to_base64_img(mock_pdf)

    mock_convert_from_bytes.assert_called_once()
    assert isinstance(result, str)
    assert len(result) > 0


@patch("file_handler.FileHandler.image_to_base64_img")
@patch("PIL.Image.open")
def test_process_uploaded_file_image(mock_image_open, mock_image_to_base64_img):
    # Mock image file
    mock_file = Mock()
    mock_file.type = "image/png"
    mock_image = Image.new("RGB", (100, 100), color="green")
    mock_image_open.return_value = mock_image
    mock_image_to_base64_img.return_value = "mock_base64_image"

    result = FileHandler.process_uploaded_file(mock_file)

    mock_image_open.assert_called_once_with(mock_file)
    mock_image_to_base64_img.assert_called_once_with(mock_image)
    assert result == "mock_base64_image"


@patch("file_handler.FileHandler.pdf_to_base64_img")
def test_process_uploaded_file_pdf(mock_pdf_to_base64_img):
    # Mock PDF file
    mock_file = Mock()
    mock_file.type = "application/pdf"
    mock_pdf_to_base64_img.return_value = "mock_base64_pdf"

    result = FileHandler.process_uploaded_file(mock_file)

    mock_pdf_to_base64_img.assert_called_once_with(mock_file)
    assert result == "mock_base64_pdf"
