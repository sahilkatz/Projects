import streamlit as st
from joblib import load
import string

# Load model and vectorizer
model = load('emotion_logistic_model.pkl')
vectorizer = load('emotion_tfidf_vectorizer.pkl')

# Optional label mapping
try:
    label_map = load('emotion_label_mapping.pkl')
    reverse_map = {v: k for k, v in label_map.items()}
except:
    reverse_map = None

# Emojis for emotions
emotion_emoji = {
    "joy": "😄", "sadness": "😢", "anger": "😡",
    "fear": "😱", "love": "❤️", "surprise": "😲"
}

# Text preprocessing
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# --- Page Config ---
st.set_page_config(page_title="Emotion Predictor", page_icon="🌙", layout="centered")

# --- Dark Theme Style ---
st.markdown(
    """
    <style>
    html, body, .stApp {
        background-color: #0f1117;
        color: #fafafa;
        font-family: 'Courier New', monospace;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 0px;
        color: #00ffe5;
    }
    .subtitle {
        text-align: center;
        font-size: 16px;
        color: #888;
        margin-top: 0px;
    }
    .emoji {
        text-align: center;
        font-size: 52px;
        margin-top: 15px;
    }
    .stTextArea textarea {
        background-color: #1e1f26;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown('<div class="title">🔮 Emotion Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Let AI detect how you feel using text</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Input Text Box ---
user_input = st.text_area("✍️ Type something...", height=150)

# --- Predict Button ---
if st.button("🚀 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter text to analyze.")
    else:
        cleaned = clean_text(user_input)
        transformed = vectorizer.transform([cleaned])
        prediction = model.predict(transformed)[0]

        emotion = reverse_map[prediction] if reverse_map else str(prediction)
        emoji = emotion_emoji.get(emotion.lower(), "💬")

        st.markdown(f'<div class="emoji">{emoji}</div>', unsafe_allow_html=True)
        st.success(f"**Predicted Emotion:** `{emotion.capitalize()}`")
