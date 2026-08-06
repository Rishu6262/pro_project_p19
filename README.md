# 📧 Spam Email Classifier Using Deep Learning

---

# 🚀 Live Demo

Experience the **Spam Email Classifier Using Deep Learning** through the interactive Streamlit web application.

🌐 **Live Application:**  
🔗 https://proprojectp19-uxf8aemmhm6lph4tcntwrx.streamlit.app/

The application allows users to enter email content and instantly predict whether the message is **Spam 🚫** or **Ham (Not Spam) ✅** using a trained **Deep Learning** model powered by **Natural Language Processing (NLP)**. Built with **Python**, **TensorFlow/Keras**, and **Streamlit**, it provides a fast, user-friendly interface for real-time email classification.

---

### ✨ Features

- 📧 Real-Time Spam Email Detection
- 🤖 Deep Learning-Based Text Classification
- 🧠 Natural Language Processing (NLP)
- ⚡ Instant Spam/Ham Prediction
- 🌐 Interactive Streamlit Web Application
- 📱 Accessible from Any Modern Web Browser

> **Try the live application and explore how Deep Learning and NLP can intelligently classify emails with just a few clicks!**

---

## 📌 Project Overview

The **Spam Email Classifier Using Deep Learning** is an **End-to-End Deep Learning and Natural Language Processing (NLP)** project designed to automatically classify emails as **Spam** or **Ham (Not Spam)**. The system leverages advanced text processing techniques and deep learning models to analyze email content and accurately detect unwanted or malicious messages.

The project utilizes **Python**, **TensorFlow/Keras**, **Natural Language Processing (NLP)**, **Tokenization**, **Text Vectorization**, and **Deep Learning** to preprocess email text, convert it into numerical representations, and train a neural network capable of distinguishing between legitimate and spam emails.

Before model training, the email dataset undergoes comprehensive **data cleaning**, **text preprocessing**, **tokenization**, **stop-word removal**, **text normalization**, and **sequence padding** to improve model performance and prediction accuracy. The trained deep learning model learns linguistic patterns commonly found in spam emails and classifies new emails in real time.

The final model can be integrated into an interactive **Streamlit web application**, allowing users to enter email content and instantly determine whether it is **Spam** or **Ham**. This project demonstrates practical expertise in **Deep Learning**, **Natural Language Processing (NLP)**, **Text Classification**, **Neural Networks**, **Python Development**, and **AI-powered Email Filtering**, making it an excellent portfolio project for aspiring **AI Engineers**, **Machine Learning Engineers**, **Deep Learning Engineers**, **NLP Engineers**, and **Data Scientists**.

---

# 💡 Why Choose This Project?

Email spam is one of the biggest challenges in modern digital communication. Every day, individuals and organizations receive thousands of unwanted emails containing advertisements, phishing attempts, malware, and fraudulent content. Manually identifying and filtering these emails is inefficient, time-consuming, and prone to human error.

The **Spam Email Classifier Using Deep Learning** addresses this challenge by leveraging **Natural Language Processing (NLP)** and **Deep Learning** techniques to automatically classify emails as **Spam** or **Ham (Not Spam)**. The system learns hidden patterns from email text, enabling accurate and intelligent email filtering.

### ⭐ Why I Chose This Project

- 📧 Solve a real-world spam detection problem.
- 🧠 Learn Natural Language Processing (NLP) concepts.
- 🤖 Explore Deep Learning models such as RNN, LSTM, and GRU.
- 📝 Work with real-world text datasets.
- 📊 Practice text preprocessing and tokenization.
- 🚀 Build an end-to-end AI-powered text classification system.
- 🌐 Develop an interactive Streamlit application.
- 💻 Strengthen practical skills in Python, Deep Learning, and NLP.

---

# 🎯 Project Objectives

The primary objective of this project is to develop an intelligent **Deep Learning-based Email Classification System** capable of accurately identifying spam emails using Natural Language Processing techniques.

### ⭐ Key Objectives

- 📧 Automatically classify emails as Spam or Ham.
- 🧹 Perform text cleaning and preprocessing.
- 🔤 Apply tokenization and sequence generation.
- 🧠 Train Deep Learning models for text classification.
- 📊 Compare RNN, LSTM, and GRU models.
- 📏 Evaluate model performance using standard classification metrics.
- 💾 Save the best-performing model for deployment.
- 🌐 Develop an interactive Streamlit application.
- 🚀 Build a deployment-ready AI-powered email filtering solution.
---

# 📂 Dataset Information

The project uses a **Spam Email Dataset** containing labeled email messages used for binary text classification.

## 📊 Dataset Summary

| Attribute | Details |
|-----------|---------|
| 📂 Dataset Name | Spam Mail Classifier Dataset |
| 📄 Total Records | **1000 Emails** |
| 📋 Total Features | **2** |
| 🎯 Target Variable | **Spam / Ham** |
| 📚 Dataset Type | Text Classification Dataset |
| 📧 Domain | Email Security & NLP |
### Target Variable

* Spam
* Ham

---

## 📋 Dataset Features

| Feature | Description |
|---------|-------------|
| 📧 email_text | Complete email content |
| 🏷 label | Spam or Ham (Target Variable) |

---

# 🛠 Technologies Used

| Category | Technology | Purpose |
|----------|------------|---------|
| 🐍 Programming Language | Python | Core development |
| 📊 Data Processing | Pandas | Data manipulation |
| 🔢 Numerical Computing | NumPy | Numerical operations |
| 🤖 Deep Learning | TensorFlow | Neural network training |
| 🧠 Deep Learning API | Keras | Model building |
| 📚 NLP | Tokenization & Text Processing | Email preprocessing |
| 💾 Model Serialization | Pickle | Save tokenizer and model |
| 🌐 Web Application | Streamlit | Interactive UI |
| 🔗 Version Control | Git & GitHub | Source code management |

---

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

# 🔄 Project Workflow

### 📥 Step 1: Data Collection

- Load the spam email dataset.
- Understand dataset structure and labels.

---

### 🧹 Step 2: Data Preprocessing

- Convert text to lowercase
- Remove punctuation
- Remove special characters
- Tokenization
- Padding sequences
- Label Encoding

---

### 📊 Step 3: Exploratory Data Analysis (EDA)

Analyze:

- Spam vs Ham distribution
- Word frequency
- Message length
- Common spam keywords

---

### 🧠 Step 4: Deep Learning Model Training

Train multiple Deep Learning models:

- Simple RNN
- LSTM
- GRU

---

### 📏 Step 5: Model Evaluation

Evaluate using:

- Accuracy
- Precision
- Recall
- F1 Score
- Loss

---

### 💾 Step 6: Model Saving

Save the trained model and tokenizer using Pickle/Keras.

---

### 🌐 Step 7: Deployment

Deploy the model using Streamlit for real-time spam prediction.

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

# 🎓 Learning Outcomes

Through this project, the following skills were developed:

- 🧠 Natural Language Processing (NLP)
- 🤖 Deep Learning
- 🔤 Text Tokenization
- 📝 Text Preprocessing
- 📊 Text Classification
- 🔄 RNN Architecture
- 🧠 LSTM Networks
- ⚡ GRU Networks
- 💾 Model Serialization
- 🌐 Streamlit Deployment

---

---

# 🚀 Future Improvements

Future enhancements include:

- 🤖 BERT-based Spam Detection
- 🧠 Transformer Models
- 🌍 Multi-language Email Support
- 📧 Gmail API Integration
- ⚡ Real-Time Email Filtering
- ☁ Cloud Deployment
- 📊 Spam Analytics Dashboard
- 📱 Mobile Application Support

---

# 📜 Disclaimer

This project has been developed solely for **educational**, **learning**, and **portfolio** purposes to demonstrate the practical implementation of **Deep Learning** and **Natural Language Processing (NLP)** for spam email classification.

The predictions generated by the model are based on patterns learned from the training dataset and may not always achieve **100% accuracy** when applied to unseen or real-world emails. Prediction performance depends on the quality, diversity, and distribution of the input data.

This application is intended to showcase concepts such as **text preprocessing**, **tokenization**, **Deep Learning-based text classification**, and **AI-powered email filtering**. It should not be considered a replacement for enterprise-grade email security or commercial spam detection systems.
---

# ✅ Conclusion

The **Spam Email Classifier Using Deep Learning** successfully demonstrates how **Artificial Intelligence**, **Deep Learning**, and **Natural Language Processing (NLP)** can be applied to automatically classify emails as **Spam** or **Ham (Not Spam)**. By utilizing advanced text preprocessing techniques and training neural network architectures such as **Simple RNN**, **LSTM**, and **GRU**, the system effectively learns hidden patterns in email content and delivers accurate spam detection.

The project showcases practical expertise in **Python**, **TensorFlow**, **Keras**, **Natural Language Processing**, **Deep Learning**, **Text Classification**, and **Streamlit Application Development**, making it a valuable portfolio project for aspiring **AI Engineers**, **Machine Learning Engineers**, **Deep Learning Engineers**, **NLP Engineers**, and **Data Scientists**.

---

# 👨‍💻 Author

## Rishu Gurjar

🎓 **B.Tech Computer Science Engineering Student**

💻 **Python Developer | Data Analyst | Machine Learning Enthusiast | Deep Learning Learner | NLP Enthusiast | Generative AI Enthusiast**

I am passionate about building intelligent applications using **Python**, **Machine Learning**, **Deep Learning**, **Natural Language Processing (NLP)**, **Generative AI**, and **Data Analytics**. I enjoy developing end-to-end AI solutions, intelligent automation systems, predictive models, and interactive web applications that solve real-world problems.

### 🚀 Technical Skills

- 🐍 Python Programming
- 🤖 Machine Learning
- 🧠 Deep Learning
- 📚 Natural Language Processing (NLP)
- 📊 Data Analysis
- 🌐 Streamlit
- 🔗 Git & GitHub

### 📬 Connect With Me

- 💻 **GitHub:** https://github.com/Rishu6262
- 💼 **LinkedIn:** https://www.linkedin.com/in/rishu-gurjar-58072a333/
- 📊 **Kaggle:** https://www.kaggle.com/rishugurjar

⭐ **If you found this project useful, consider giving it a Star ⭐ on GitHub. Your support and feedback are greatly appreciated!**

# 👨‍💻 Author

**Rishu Gurjar**

Aspiring Data Science | Machine Learning Enthusiast | Deep Learning Developer
