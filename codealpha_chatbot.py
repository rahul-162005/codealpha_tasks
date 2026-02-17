import streamlit as st
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# ---------------- FAQ DATA ----------------
faqs = {
    "What is this service about?":
        "This service provides users with online tools and support to manage their accounts and access various features.",

    "How do I create an account?":
        "To create an account, click on the Sign Up button and fill in your details such as name, email, and password.",

    "How do I reset my password?":
        "Click on the 'Forgot Password' option on the login page and follow the instructions sent to your email.",

    "How can I contact customer support?":
        "You can contact customer support through the Contact Us page or by emailing support@example.com.",

    "Is my personal information secure?":
        "Yes, we use secure encryption and follow industry standards to protect your personal information."
}

# ---------------- PREPROCESS ----------------
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Prepare vectors
questions = list(faqs.keys())
answers = list(faqs.values())
processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

# ---------------- RESPONSE FUNCTION ----------------
def get_response(user_input):
    user_input_processed = preprocess(user_input)
    user_vector = vectorizer.transform([user_input_processed])
    similarity = cosine_similarity(user_vector, X)
    best_match_index = similarity.argmax()

    if similarity[0][best_match_index] < 0.2:
        return "Sorry, I couldn't understand your question."

    return answers[best_match_index]

# ---------------- STREAMLIT UI ----------------
st.title("🤖 AI FAQ Chatbot")
st.write("Ask your question below:")

user_input = st.text_input("You:")

if user_input:
    response = get_response(user_input)
    st.write("Bot:", response)
