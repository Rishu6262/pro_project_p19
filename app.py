import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = load_model("email_classifier.h5")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 50  # same as used in training

st.set_page_config(page_title="Email Spam Classifier", layout="centered")

st.title("📧 Email Spam Classifier")
st.write("Check whether an email is **Spam** or **Not Spam**")

# Input text
email_text = st.text_area("✍️ Enter Email Content", height=200)

if st.button("🔍 Predict"):
    if email_text.strip() == "":
        st.warning("Please enter email text")
    else:
        # Preprocessing
        seq = tokenizer.texts_to_sequences([email_text])
        padded = pad_sequences(seq, maxlen=MAX_LEN)

        # Prediction
        pred = model.predict(padded)[0][0]

        if pred > 0.5:
            st.error(f"🚨 Spam Email ({pred:.2f})")
        else:
            st.success(f"✅ Not Spam ({1-pred:.2f})")
