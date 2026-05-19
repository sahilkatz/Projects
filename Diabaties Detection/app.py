import streamlit as st
import numpy as np
import joblib
import time

# Load model and scaler
model = joblib.load("NB_dia.pkl")
scaler = joblib.load("scaler.pkl")

# ------------------ Styling ------------------
st.set_page_config(page_title="DiaScan", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
    html, body {
        background-color: #0f172a;
    }

    h1, h4 {
        color: white !important;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        text-shadow: 0 0 15px #38bdf8;
        font-size: 3rem;
        margin-bottom: 0;
    }

    .stSlider > div {
        color: #f8fafc;
        font-weight: 600;
    }

    .stButton button {
        background: linear-gradient(to right, #14b8a6, #0ea5e9);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6em 2em;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
        margin-top: 20px;
    }

    .stButton button:hover {
        background: linear-gradient(to right, #0ea5e9, #14b8a6);
        transform: scale(1.05);
        box-shadow: 0 0 12px #38bdf8;
    }

    .prediction-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        text-align: center;
        color: white;
        box-shadow: 0 0 10px #0ea5e9;
    }

    .footer {
        text-align: center;
        font-size: 12px;
        color: #94a3b8;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown("<h1>🩺 DiaScan</h1>", unsafe_allow_html=True)
st.markdown("<h4>Early Diabetes Risk Predictor</h4>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #1e3a8a;'>", unsafe_allow_html=True)

# ------------------ Inputs ------------------
st.markdown("### 👉 Enter your health parameters:")

glucose = st.slider("Glucose Level (mg/dL)", 50, 200, 100)
insulin = st.slider("Insulin Level (mu U/mL)", 15, 846, 80)
bmi = st.slider("BMI (kg/m²)", 10.0, 60.0, 25.0)
age = st.slider("Age (years)", 18, 80, 30)
preg = st.slider("Pregnancies", 0, 15, 1)
dpf = st.slider("Diabetes Pedigree Function", 0.05, 2.5, 0.5)

# ------------------ Prediction Logic ------------------
input_data = np.array([[preg, glucose, insulin, bmi, dpf, age]])
scaled_data = scaler.transform(input_data)

if st.button("🔍 Predict My Risk"):
    with st.spinner("🧠 Analyzing your health profile..."):
        time.sleep(1.5)  # Animation effect

    result = model.predict(scaled_data)[0]

    # Output Result
    if result == 1:
        st.markdown(
            "<div class='prediction-box'><h3 style='color:#f87171;'>🚨 High Risk of Diabetes</h3><p>Please consult a doctor for proper diagnosis and management.</p></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='prediction-box'><h3 style='color:#4ade80;'>✅ Low Risk of Diabetes</h3><p>You're doing well! Keep up a healthy lifestyle. 🥗🏃‍♂️</p></div>",
            unsafe_allow_html=True
        )

    # Smart Tips
    st.markdown("### 🧾 Health Tips Based on Your Inputs:")
    if bmi >= 30:
        st.warning("⚠️ Your BMI is high. Consider a balanced diet and regular exercise.")
    if glucose > 150:
        st.warning("⚠️ High glucose levels detected. Consider reducing sugar intake.")
    if age > 50:
        st.info("🔎 Over 50? Routine checkups are strongly recommended.")
    if (
    glucose <= 120 and
    bmi <= 25 and
    40 <= insulin <= 160 and
    age < 40 and
    dpf <= 0.7
):
        
     st.markdown(
        "<div class='prediction-box' style='background-color:#064e3b;box-shadow:0 0 12px #10b981;'>"
        "<h3 style='color:#bbf7d0;'>🌟 You're in great shape!</h3>"
        "<p style='color:#d1fae5;'>Keep maintaining this healthy lifestyle! 💪🥗🏃‍♂️</p>"
        "</div>",
        unsafe_allow_html=True
     )
# ------------------ Footer ------------------
st.markdown("<div class='footer'>⚠️ This tool is for educational purposes and does not replace professional medical advice.</div>", unsafe_allow_html=True)
