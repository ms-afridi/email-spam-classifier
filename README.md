# 📩 Email Spam Classifier (NLP + Machine Learning)

This project is an end-to-end **Email Spam Detection System** built using **Natural Language Processing (NLP)** and **Machine Learning**, and deployed as a web application using **Streamlit**.

The system classifies an email as **Spam** or **Not Spam (Ham)** based on its textual content.

---

## 🚀 Features

* Text preprocessing using NLP techniques
* Email vectorization using **CountVectorizer**
* Classification using **Multinomial Naive Bayes**
* Interactive web interface built with **Streamlit**
* Trained model and vectorizer saved for reuse
* Clean and modular project structure

---

## 🧠 Tech Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **NLP:** NLTK
* **Visualization:** Matplotlib, Seaborn
* **Web App:** Streamlit

---

## 📂 Project Structure

```
email-spam-classifier/
│
├── app.py                     # Streamlit application
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
│
├── models/                    # Trained model artifacts
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/                 # Jupyter notebooks
│   └── training.ipynb
│
├── data/                      # Dataset (if applicable)
   └── spam.csv
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download NLTK stopwords

```python
import nltk
nltk.download("stopwords")
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 🧪 Example

**Spam Email**

> *Congratulations! You have won a cash prize. Click the link below to claim now.*

**Prediction:** 🚨 Spam

---

## 📊 Model Overview

* **Vectorizer:** CountVectorizer with custom text preprocessing
* **Classifier:** Multinomial Naive Bayes
* **Evaluation Metrics:**

  * Accuracy
  * Confusion Matrix
  * Classification Report

---

## 📌 Future Improvements

* Use `Pipeline` to combine preprocessing and modeling
* Add probability/confidence score to predictions
* Support email file uploads (.txt)
* Deploy on Streamlit Cloud or Hugging Face Spaces
* Replace custom preprocessing with built-in vectorizer options

---

## 👤 Author

**Md Shahid Afridi**

* MSc in Big Data Analytics
* AI / Machine Learning Engineer
* LinkedIn: [https://linkedin.com/in/mdshahidafridi](https://linkedin.com/in/mdshahidafridi)

---

## 📜 License

This project is open-source and available for educational and research purposes.

---

⭐ If you found this project helpful, feel free to star the repository!
