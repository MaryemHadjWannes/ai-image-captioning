# ai_image_captioning_app.py

import streamlit as st
from PIL import Image
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    Blip2Processor,
    Blip2ForConditionalGeneration
)
import torch

st.set_page_config(page_title="AI Image Captioning", layout="centered")

st.title("📷 AI Image Captioning")
st.write("Upload an image and let the AI describe it!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Generating caption..."):
        processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
        model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xl")

        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

    st.success("Here's the AI caption:")
    st.write(f"**{caption}**")

