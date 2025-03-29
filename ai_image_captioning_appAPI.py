import streamlit as st
from PIL import Image
import requests
import io

from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")


API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip2-opt-2.7b"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_caption_blip2_flan(image: Image.Image) -> str:
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()

    # Use Flan-T5 prompting
    payload = {
        "inputs": {
            "image": img_bytes,
            "prompt": "Describe this image in detail."
        }
    }

    response = requests.post(API_URL, headers=HEADERS, files={"image": img_bytes})
    result = response.json()

    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]
    elif "error" in result:
        return f"⚠️ Error: {result['error']}"
    else:
        return "❌ Failed to get a caption."

st.set_page_config(page_title="BLIP2 + Flan-T5 Captioning", layout="centered")
st.title("🧠 BLIP2 + Flan-T5 AI Image Captioning")
st.write("Smart captioning with BLIP2 + Flan-T5 model via Hugging Face API")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Your image", use_column_width=True)

    with st.spinner("Talking to BLIP2 + Flan-T5..."):
        caption = get_caption_blip2_flan(image)

    st.success("Here's your caption:")
    st.write(f"**{caption}**")

