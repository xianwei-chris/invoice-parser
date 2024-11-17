import streamlit as st
import pandas as pd
import json
from file_handler import FileHandler
from genai_handler import GenAIHandler


class InvoiceParserApp:
    """
    Main application class for the Invoice Parser.
    Handles file upload, processing, and field extraction.
    """

    def __init__(self):
        self.uploaded_file = None
        self.genai_handler = GenAIHandler()

    def display_header(self):
        """Displays the header section of the app."""
        st.title("Invoice Parser")
        st.header("Upload Invoice")
        st.write(
            "Upload a PDF or image file of your invoice to begin the extraction process"
        )

    def upload_file(self):
        """Handles file upload from the user."""
        self.uploaded_file = st.file_uploader(
            "Upload a PDF or Image", type=["pdf", "png", "jpg", "jpeg"]
        )

    def process_and_display_invoice(self):
        """Processes the uploaded file and displays the extracted invoice fields."""
        button = st.button("Confirm")

        if button and self.uploaded_file is not None:
            st.subheader("File Type and Processing")
            st.write(f"Uploaded file type: {self.uploaded_file.type}")
            st.write("Processing...")

            try:
                # Process the file
                img_base64 = FileHandler.process_uploaded_file(self.uploaded_file)
                st.image(
                    "data:image/png;base64," + img_base64, use_container_width=True
                )

                # Extract fields using GenAI
                st.header("Extracted Fields")
                st.write(
                    "Extracting fields and line items from the uploaded document..."
                )
                json_resp = self.genai_handler.parse_invoice(img_base64)

                # Display extracted fields
                st.write("Key fields extracted from the invoice:")
                st.write(json_resp)

                # Display line items
                st.write("Line items:")
                if "line_items" in json_resp and json_resp["line_items"]:
                    df = pd.DataFrame(json_resp["line_items"])
                    st.write(df)
                else:
                    st.write("No line items found in the invoice.")

            except json.JSONDecodeError as e:
                st.error(
                    f"Sorry, the response from the extraction function is not valid JSON, error: {e}"
                )
            except Exception as e:
                st.error(f"Sorry, an unexpected error occurred: {e}")

    def run(self):
        """Runs the main application."""
        self.display_header()
        self.upload_file()
        self.process_and_display_invoice()


# Run the application
if __name__ == "__main__":
    app = InvoiceParserApp()
    app.run()
