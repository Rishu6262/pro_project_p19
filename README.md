# 📧 Spam Email Classifier Using Deep Learning

## 📌 Project Overview

The **Spam Email Classifier Using Deep Learning** is an **End-to-End Deep Learning and Natural Language Processing (NLP)** project designed to automatically classify emails as **Spam** or **Ham (Not Spam)**. The system leverages advanced text processing techniques and deep learning models to analyze email content and accurately detect unwanted or malicious messages.

The project utilizes **Python**, **TensorFlow/Keras**, **Natural Language Processing (NLP)**, **Tokenization**, **Text Vectorization**, and **Deep Learning** to preprocess email text, convert it into numerical representations, and train a neural network capable of distinguishing between legitimate and spam emails.

Before model training, the email dataset undergoes comprehensive **data cleaning**, **text preprocessing**, **tokenization**, **stop-word removal**, **text normalization**, and **sequence padding** to improve model performance and prediction accuracy. The trained deep learning model learns linguistic patterns commonly found in spam emails and classifies new emails in real time.

The final model can be integrated into an interactive **Streamlit web application**, allowing users to enter email content and instantly determine whether it is **Spam** or **Ham**. This project demonstrates practical expertise in **Deep Learning**, **Natural Language Processing (NLP)**, **Text Classification**, **Neural Networks**, **Python Development**, and **AI-powered Email Filtering**, making it an excellent portfolio project for aspiring **AI Engineers**, **Machine Learning Engineers**, **Deep Learning Engineers**, **NLP Engineers**, and **Data Scientists**.

---

## ✨ Key Features

- 📧 Spam vs Ham Email Classification
- 🧠 Natural Language Processing (NLP)
- 🤖 Deep Learning-Based Text Classification
- 📝 Text Cleaning & Preprocessing
- 🔤 Tokenization & Text Vectorization
- 📊 Model Training & Performance Evaluation
- 💾 Model Serialization
- 🌐 Interactive Streamlit Web Application
- ⚡ Real-Time Email Prediction
- 🚀 Deployment Ready

---

# ❓ Why Use This Project?

Email spam is one of the most common problems in digital communication. Manually filtering unwanted emails is time-consuming and inefficient. This project uses Deep Learning and Natural Language Processing (NLP) techniques to automatically classify emails as Spam or Ham (Not Spam).

### Benefits of This Project

* Automates email filtering process.
* Reduces unwanted spam messages.
* Improves email management efficiency.
* Demonstrates real-world NLP applications.
* Helps organizations and individuals detect suspicious emails.
* Provides hands-on experience with Deep Learning models such as RNN, LSTM, and GRU.
* Can be extended for enterprise-level email security systems.

This project serves as a practical example of how Artificial Intelligence can be used to solve real-world communication and cybersecurity challenges.

---

❓ Why I Chose This Project?

I chose this project because email spam detection is a real-world problem that affects individuals and organizations every day. Spam emails can waste time, reduce productivity, and sometimes contain malicious content such as phishing links and scams.

This project provided an opportunity to apply Natural Language Processing (NLP) and Deep Learning techniques to solve a practical problem. It allowed me to work with text data, perform preprocessing and tokenization, and build advanced models such as RNN, LSTM, and GRU for email classification.

Through this project, I gained hands-on experience in data preprocessing, deep learning model development, performance evaluation, and deployment. It also helped me strengthen my understanding of how Artificial Intelligence can be used to automate tasks and improve communication systems.

---

# 🚀 Objectives

* Detect spam emails automatically.
* Apply Natural Language Processing techniques.
* Train Deep Learning models for text classification.
* Compare model performance.
* Build a reusable email filtering system.

---

# 📊 Dataset Information

### Dataset Name

Spam Mail Classifier Dataset

### Total Records

* 1000 Emails

### Features

| Feature    | Description   |
| ---------- | ------------- |
| email_text | Email Content |
| label      | Spam or Ham   |

### Target Variable

* Spam
* Ham

---

# 🛠 Technologies Used

* Python
* NumPy
* Pandas
* TensorFlow
* Keras
* NLP
* Streamlit
* Pickle

---

# 📂 Project Structure

```bash
Spam_Email_Classifier/
│
├── app.py
├── email_classifier.h5
├── tokenizer.pkl
├── spam_mail_classifier.csv
├── requirements.txt
├── README.md
│
└── notebooks/
    └── model_training.ipynb
```

---

# 🔍 Data Preprocessing

The following preprocessing steps were applied:

* Lowercase Conversion
* Text Cleaning
* Removing Special Characters
* Tokenization
* Sequence Padding
* Label Encoding

---

# 🤖 Deep Learning Models Used

## 1. Simple RNN

Advantages:

* Learns sequential text patterns
* Fast training

---

## 2. LSTM

Advantages:

* Handles long-term dependencies
* Better text understanding

---

## 3. GRU

Advantages:

* Faster than LSTM
* Efficient memory usage

---

# ⚙️ Model Workflow

1. Load Dataset
2. Clean Email Text
3. Tokenize Text
4. Convert Text into Sequences
5. Apply Padding
6. Train Deep Learning Models
7. Evaluate Performance
8. Save Best Model
9. Predict Spam/Ham Emails

---

# 📈 Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Loss

---

# 🏆 Best Model Selection

The following models were compared:

* RNN
* LSTM
* GRU

The model with the highest validation accuracy was selected and saved for deployment.

---

# 💻 Streamlit Application

Users can:

* Enter Email Text
* Click Predict
* Instantly Get Results

Prediction Output:

* Spam Email 🚫
* Ham Email ✅

---

# ▶️ Run Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
tensorflow
numpy
pickle-mixin
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Natural Language Processing
* Text Preprocessing
* Tokenization
* Deep Learning
* RNN
* LSTM
* GRU
* TensorFlow
* Model Deployment
* Streamlit

---

# 🔮 Future Improvements

* BERT-based Spam Detection
* Multi-language Support
* Real-time Email Filtering
* Gmail Integration
* Advanced NLP Models

---

# 📜 Disclaimer

This project is developed for educational and research purposes only.

The predictions generated by the model are based on learned patterns from historical email data and may not always be 100% accurate. The system is intended to demonstrate the application of Deep Learning and NLP techniques in spam email detection.

---

# Conclusion

This project demonstrates how Deep Learning and Natural Language Processing can be used to automatically classify emails as Spam or Ham. By leveraging models such as RNN, LSTM, and GRU, the system effectively learns patterns in email text and provides accurate predictions for email filtering applications.

---

# 👨‍💻 Author

**Rishu Gurjar**

Aspiring Data Scientist | Machine Learning Enthusiast | Deep Learning Developer
