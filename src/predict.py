import os
from openai import OpenAI
from dotenv import load_dotenv

import prompt
import constants

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_fields_with_genai(base64_image):
    try:
        response = client.chat.completions.create(
            model=constants.MODEL,
            messages=[
                {"role": "system", "content": f"{prompt.SYSTEM_MESSAGE}"},
                {"role": "user", "content": [
                    {"type": "text", "text": f"{prompt.EXTRACTION_PROMPT}"},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"}
                    }
                ]}
            ],
            temperature=0.0,
        )    
        return response.choices[0].message.content
    
    except Exception as e:
        return f"An error occurred: {e}"