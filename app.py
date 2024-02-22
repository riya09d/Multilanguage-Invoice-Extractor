import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load gemini pro vision model
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, user_prompt):
    response = model.generate_content([input, image[0], user_prompt])
    return response.text
    
def input_image_details(uploaded_file):
    # Check if uploaded file is None
    if uploaded_file is None:
        raise FileNotFoundError('No such file exists')

    # Reading file into bytes
    bytes_data = uploaded_file.getvalue()

    image_parts = [
        {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
    ]
    return image_parts

# Initializing Streamlit app
st.set_page_config(page_title='MultiLanguage Invoice Extractor')

st.header('MultiLanguage Invoice Extractor')
input = st.text_input('Input prompt:', key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=['jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload a image as invoice and you will have to answer questions based on the uploaded image"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader('According to the Invoice: ')
    st.write(response)
