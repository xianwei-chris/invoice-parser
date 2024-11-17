import pytest
from unittest.mock import patch, Mock

from app import InvoiceParserApp


@pytest.fixture
def app():
    return InvoiceParserApp()


@patch("file_handler.FileHandler.process_uploaded_file")
@patch("genai_handler.GenAIHandler.parse_invoice")
@patch("streamlit.image")
@patch("streamlit.file_uploader")
@patch("streamlit.button")
def test_process_and_display_invoice(
    mock_button,
    mock_file_uploader,
    mock_image,
    mock_parse_invoice,
    mock_process_uploaded_file,
    app,
):
    # Mock Streamlit components
    mock_button.return_value = True
    mock_file_uploader.return_value = Mock(type="image/png")
    mock_process_uploaded_file.return_value = "mock_base64_image"
    mock_parse_invoice.return_value = {
        "field": "value",
        "line_items": [{"item": "item1", "price": 10}],
    }

    # Run the process method
    app.upload_file()
    app.process_and_display_invoice()

    # Assertions
    mock_file_uploader.assert_called_once()
    mock_button.assert_called_once()
    mock_process_uploaded_file.assert_called_once()
    mock_parse_invoice.assert_called_once_with("mock_base64_image")
