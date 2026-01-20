import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

# ---- SAME process() used during training ----
def process(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    clean = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean

# ---- Load vectorizer & model ----
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
model = pickle.load(open("models/model.pkl", "rb"))

# ---- Streamlit UI ----
st.title("📩 Email Spam Classifier")

user_input = st.text_area("Enter the email content:")

if st.button("Check Spam"):
    if user_input.strip() == "":
        st.warning("Please enter some email text.")
    else:
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)

        if prediction[0] == 1:
            st.error("🚨 This is a SPAM email!")
        else:
            st.success("✅ This is NOT a spam email.")
