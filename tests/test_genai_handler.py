import pytest
from unittest.mock import Mock
import json

from genai_handler import GenAIHandler


@pytest.fixture
def handler():
    """
    Fixture to initialize the GenAIHandler with a mocked client.
    """
    handler = GenAIHandler()
    handler.client = Mock()
    return handler


def test_parse_invoice(handler):
    """
    Test the parse_invoice method with a mocked client.
    """
    # Mock the response from the OpenAI API
    mock_response = Mock()
    mock_choice = Mock()
    mock_message = Mock()

    mock_json_response = {
        "invoice_number": "12345",
        "amount": "100.00",
        "date": "2024-11-17",
    }

    # Set up the mocked response structure
    mock_message.content = json.dumps(mock_json_response)
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]

    # Configure the mocked client's behavior
    handler.client.chat.completions.create.return_value = mock_response

    # Base64 image input for testing
    base64_image = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgAAAAAgAB9HFkqAAAAABJRU5ErkJggg=="

    # Call the method
    result = handler.parse_invoice(base64_image)

    # Assertions
    assert result == mock_json_response
    handler.client.chat.completions.create.assert_called_once_with(
        model=handler.model,
        messages=[
            {"role": "system", "content": handler.system_message},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": handler.extraction_prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                    },
                ],
            },
        ],
        temperature=0.0,
    )
