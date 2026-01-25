# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# this is simple ui for project 
# and this project ui only for show a mail spam or not spam mail

# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# import streamlit as st
# import pickle
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# # Load model
# model = load_model("email_classifer.h5")

# # Load tokenizer
# with open("tokenizer.pkl", "rb") as f:
#     tokenizer = pickle.load(f)

# MAX_LEN = 50  # same as used in training

# st.set_page_config(page_title="Email Spam Classifier", layout="centered")

# st.title("📧 Email Spam Classifier")
# st.write("Check whether an email is **Spam** or **Not Spam**")

# # Input text
# email_text = st.text_area("✍️ Enter Email Content", height=200)

# if st.button("🔍 Predict"):
#     if email_text.strip() == "":
#         st.warning("Please enter email text")
#     else:
#         # Preprocessing
#         seq = tokenizer.texts_to_sequences([email_text])
#         padded = pad_sequences(seq, maxlen=MAX_LEN)

#         # Prediction
#         pred = model.predict(padded)[0][0]

#         if pred > 0.5:
#             st.error(f"🚨 Spam Email ({pred:.2f})")
#         else:
#             st.success(f"✅ Not Spam ({1-pred:.2f})")

# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# this is a new simple ui for project 
# and this project ui only for show a mail spam or not spam mail with percenatge probability 

# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
import streamlit as st
import pickle
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ------------------ CONFIG ------------------
MODEL_PATH = "email_classifer.h5"   # ✅ SAME AS YOUR FILE
TOKENIZER_PATH = "tokenizer.pkl"
MAX_LEN = 50
SPAM_THRESHOLD = 0.65
# --------------------------------------------

st.set_page_config(
    page_title="Email Spam Classifier",
    layout="centered"
)

st.title("📧 Email Spam Classifier")
st.write("Check whether an email is **Spam** or **Not Spam**")

# ------------------ LOAD FILES SAFELY ------------------
if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file (email_classifer.h5) not found")
    st.stop()

if not os.path.exists(TOKENIZER_PATH):
    st.error("❌ Tokenizer file (tokenizer.pkl) not found")
    st.stop()

# ✅ CORRECT LOADING
model = load_model(MODEL_PATH)

with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

# ------------------ INPUT ------------------
email_text = st.text_area(
    "✍️ Enter Email Content",
    height=200
)

# ------------------ PREDICT ------------------
if st.button("🔍 Predict"):
    if email_text.strip() == "":
        st.warning("⚠️ Please enter email text")
    else:
        seq = tokenizer.texts_to_sequences([email_text])
        padded = pad_sequences(seq, maxlen=MAX_LEN)

        pred = model.predict(padded, verbose=0)[0][0]

        spam_prob = float(pred)
        not_spam_prob = 1 - spam_prob

        spam_percent = spam_prob * 100
        not_spam_percent = not_spam_prob * 100

        st.subheader("📊 Prediction Result")

        if spam_prob >= SPAM_THRESHOLD:
            st.error(
                f"🚨 **Spam Email**\n\n"
                f"📌 Spam Probability: **{spam_percent:.2f}%**\n"
                f"📌 Not Spam Probability: **{not_spam_percent:.2f}%**"
            )

        elif spam_prob >= 0.50:
            st.warning(
                f"⚠️ **Possibly Spam (Borderline Case)**\n\n"
                f"📌 Spam Probability: **{spam_percent:.2f}%**\n"
                f"📌 Not Spam Probability: **{not_spam_percent:.2f}%**"
            )

        else:
            st.success(
                f"✅ **Not Spam Email**\n\n"
                f"📌 Spam Probability: **{spam_percent:.2f}%**\n"
                f"📌 Not Spam Probability: **{not_spam_percent:.2f}%**"
            )
# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

