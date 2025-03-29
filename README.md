# 📷 AI Image Captioning App

A simple Streamlit app that uses the BLIP model to generate captions for any uploaded image.

## 🚀 How It Works
1. Upload an image (jpg/png)
2. The AI model will analyze it
3. You’ll get a descriptive caption like:  
   > “A cat wearing sunglasses while sitting on a couch.”

## 🧠 Tech Stack
- Python
- Streamlit
- Transformers (BLIP model from Salesforce)
- Hugging Face

## 🛠️ Run Locally

```bash
pip install streamlit transformers torch torchvision Pillow
streamlit run ai_image_captioning_app.py
```
## 🧠 Model Comparison: BLIP Base vs Large vs BLIP2
We tested the same image using 3 different models. Here's how their descriptions differ:

### 🏃 Input Image:
![image1](https://github.com/user-attachments/assets/933dbcbe-0dd6-4917-a3bf-bfc4d862d244)





