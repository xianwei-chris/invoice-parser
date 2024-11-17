import json
from dotenv import load_dotenv
import os
from openai import OpenAI
import prompt

import constants


# Load environment variables
load_dotenv()


class GenAIHandler:
    """
    Handles interaction with OpenAI's API for processing tasks.
    """

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = constants.MODEL
        self.system_message = prompt.SYSTEM_MESSAGE
        self.extraction_prompt = prompt.EXTRACTION_PROMPT

    def _extract_fields_with_genai(self, base64_image):
        """
        Extract fields from a base64-encoded image using OpenAI's API.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"{self.system_message}"},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"{self.extraction_prompt}"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                    ],
                },
            ],
            temperature=0.0,
        )

        return response.choices[0].message.content

    def parse_invoice(self, base64_image):
        """
        Parse an invoice from a base64-encoded image using GenAI.
        Returns extracted fields as a JSON object.
        """
        try:
            text = self._extract_fields_with_genai(base64_image)
            return json.loads(text)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Error parsing JSON response: {e}, OpenAI response: {text}"
            )
