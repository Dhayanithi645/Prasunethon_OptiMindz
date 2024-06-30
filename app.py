import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Define the model and tokenizer paths
model_path = r"D:\Prasunethon_Badaga\Baduga model"

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load the model
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def translate(text):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    # Move input tensors to the same device as the model
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit app
st.set_page_config(
    page_title="Badaga to English Translator",
    page_icon=":earth_africa:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for a sleek look
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        color: #333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border: none;
        border-radius: 4px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌐 Badaga to English Translator")
st.write("Translate text from Badaga to English using a custom-trained model.")

input_text = st.text_area("Enter Badaga text here:", height=150)

if st.button("Translate"):
    if input_text.strip():
        translation = translate(input_text)
        st.write("### Translation:")
        st.write(f"**Badaga:** {input_text}")
        st.write(f"**English:** {translation}")
    else:
        st.error("Please enter some text to translate.")
