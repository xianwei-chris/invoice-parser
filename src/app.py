import streamlit as st
from PIL import Image
import pandas as pd
import json

from helper import image_to_base64_img, pdf_to_base64_img
from predict import extract_fields_with_genai

st.title("Invoice Parser")
st.header("Upload Invoice")
st.write("Upload a PDF or image file of your invoice to begin the extraction process")
uploaded_file = st.file_uploader("Upload a PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

button = st.button("Confirm")

if button and uploaded_file is not None:
    st.subheader("File Type and Processing")
    file_type = uploaded_file.type
    st.write(f"Uploaded file type: {file_type}")
    st.write("Processing...")


    if file_type == "application/pdf":
        # Process only the first page
        img_base64 = pdf_to_base64_img(uploaded_file)
    else:
        image = Image.open(uploaded_file)
        img_base64 = image_to_base64_img(image)

    # Display the image
    st.image("data:image/png;base64," + img_base64, use_container_width=True)

    st.header("Extracted Fields")    
    st.write("Extracting fields and line items from the uploaded document...")
    try:
        text = extract_fields_with_genai(img_base64)
        json_resp = json.loads(text)
        st.write("")
        st.write("Key fields extracted from the invoice:")
        st.write(json_resp)

        # Check if line items exist
        st.write("Line items:")
        if 'line_items' in json_resp and json_resp['line_items']:
            df = pd.DataFrame(json_resp['line_items'])
            st.write(df)
        else:
            st.write("No line items found in the invoice.")

    except json.JSONDecodeError:
        st.error("Sorry,the response from the extraction function is not valid JSON.")
        st.write(f"OpenAI Response: {text}")
    except Exception as e:
        st.error(f"Sorry, an unexpected error occurred: {e}")
        st.write(f"OpenAI Response: {text}")
