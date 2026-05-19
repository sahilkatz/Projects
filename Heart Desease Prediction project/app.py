import streamlit as st
import pandas as pd
import joblib

# Load your models and assets
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# --- Page Settings ---
st.set_page_config(page_title="Heart Risk Predictor", page_icon="🩺", layout="centered")

# --- Custom CSS for Styling & Animations ---
st.markdown("""
<style>
/* Background */
body {
    background-color: #1a1a1a;
}

/* Headings */
h1, h4 {
    color: white !important;
    animation: fadein 1.5s ease-in-out;
}

/* Button styling */
.stButton > button {
    background-color: transparent;
    color: white;
    border: 2px solid white;
    border-radius: 12px;
    padding: 8px 20px;
    font-weight: 600;
    transition: all 0.3s ease-in-out;
}

.stButton > button:hover {
    background-color: #ffffff;
    color: #1a1a1a;
    transform: scale(1.05);
}

/* Inputs */
.css-1cpxqw2, .stSelectbox label, .stSlider label, .stNumberInput label {
    color: white !important;
}

/* Animation */
@keyframes fadein {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='text-align: center;'>🩺 Heart Disease Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>AI Assistant for Early Cardio Detection</h4>", unsafe_allow_html=True)
st.markdown("<hr style='border-top: 1px solid white;'>", unsafe_allow_html=True)

# --- Input Section ---
st.markdown("### 🧾 Enter Patient Information", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Gender", ["M", "F"])
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

with col2:
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)

# --- Predict Button ---
if st.button("🔍 Predict"):
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Add missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    # Transform and predict
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    st.markdown("<hr style='border-top: 1px solid white;'>", unsafe_allow_html=True)

    if prediction == 1:
        st.error("⚠️ **High Risk of Heart Disease Detected!**\n\nPlease consult a cardiologist immediately.")
    else:
        st.success("✅ **Low Risk of Heart Disease.**\n\nMaintain a healthy lifestyle and have regular checkups.")

# --- Footer ---
st.markdown("<hr style='border-top: 1px solid white;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: gray;'>🔬 This tool is for educational purposes only. For medical advice, consult a certified doctor.</p>", unsafe_allow_html=True)
