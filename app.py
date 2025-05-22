import streamlit as st
import joblib
import pandas as pd

# ─── Page Config & Theme Overrides ─────────────────────────────────────────────
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS for a white, professional theme black good theme
st.markdown("""
    <style>
    /* Hide Streamlit footer & menu */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    /* Background and font */
    .css-1d391kg { background-color: #ffffff; }
    .css-18ni7ap { background-color: #ffffff; }

    /* Card container */
    .card {
        background-color: #f8f9fa;
        border: 1px solid #e3e6ea;
        border-radius: 8px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Button styling */
    .stButton > button {
        background-color: #007bff;
        color: white;
        font-size:16px;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }

    /* Result box */
    .result-box {
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        font-weight: 600;
    }
    .fraud { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
    .normal { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
    .hover-title-desc {
        transition: color 0.3s, text-shadow 0.3s, transform 0.3s;
    }
    .hover-title-desc:hover {
        color: #ff9800 !important;
        text-shadow: 0 2px 16px #ff9800, 0 0px 8px #fff;
        transform: scale(1.04) rotate(-1deg);
        cursor: pointer;
    }
    .hover-prediction-results {
        transition: color 0.3s, text-shadow 0.3s, transform 0.3s;
    }
    .hover-prediction-results:hover {
        color: #00b894 !important;
        text-shadow: 0 2px 16px #00b894, 0 0px 8px #fff;
        transform: scale(1.04) rotate(1deg);
        cursor: pointer;
    }
    .hover-fraud-count {
        transition: color 0.3s, text-shadow 0.3s, transform 0.3s;
    }
    .hover-fraud-count:hover {
        color: #d63031 !important;
        text-shadow: 0 2px 16px #d63031, 0 0px 8px #fff;
        transform: scale(1.04) rotate(-2deg);
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)


# ─── Title & Description ────────────────────────────────────────────────────────
st.markdown("<h1 class='hover-title-desc' style='text-align:center; color:#007bff;'>Credit Card Fraud Detection</h1>", unsafe_allow_html=True)
st.markdown("<p class='hover-title-desc' style='text-align:center; color:#fff; font-size:16px;'>Upload a CSV file with 29 features (V1–V28 + Amount).</p>", unsafe_allow_html=True)


# ─── Load Model ──────────────────────────────────────────────────────────────────
@st.cache_data
def load_model():
    return joblib.load("best_model.joblib")

model = load_model()


# ─── Upload & Predict for CSV ───────────────────────────────────────────────────
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Check required columns
    required_cols = [f"V{i}" for i in range(1, 29)] + ["Amount"]
    if not all(col in df.columns for col in required_cols):
        st.error("Uploaded CSV must contain exactly 29 features: V1–V28 and Amount.")
    else:
        st.success("✅ File uploaded successfully!")
        st.dataframe(df.head())

        if st.button("Predict"):
            probs = model.predict_proba(df)[:, 1]
            preds = (probs >= 0.5).astype(int)

            result_df = df.copy()
            result_df["Prediction"] = preds
            result_df["Probability"] = probs.round(4)

            st.markdown("<h3 class='hover-prediction-results' style='margin-top:2rem;'>🔍 Prediction Results</h3>", unsafe_allow_html=True)
            st.dataframe(result_df[["Prediction", "Probability"]].head())

            fraud_count = result_df["Prediction"].sum()
            total = len(result_df)
            avg_proba = result_df["Probability"].mean()
            st.markdown(f"<div class='result-box hover-fraud-count'>Fraudulent: {fraud_count} / {total}<br>Average Fraud Probability: {avg_proba:.4f}</div>", unsafe_allow_html=True)

# ─── Footer (classic bar: left=mail, center=credit, right=github) ──────────────
st.markdown("""
<style>
.footer-bar {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100vw;
    background: linear-gradient(90deg, #232526 0%, #414345 100%);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.7rem 2.5vw 0.7rem 2.5vw;
    font-size: 16px;
    z-index: 1000;
    box-shadow: 0 -2px 12px rgba(0,0,0,0.12);
    border-top: 2px solid #ff9800;
    letter-spacing: 0.5px;
}
.footer-bar .footer-left, .footer-bar .footer-center, .footer-bar .footer-right {
    display: flex;
    align-items: center;
}
.footer-bar .footer-center {
    flex: 1;
    justify-content: center;
}
.footer-bar a {
    color: #ff9800;
    text-decoration: none;
    margin: 0 8px;
    transition: color 0.2s;
    font-weight: 500;
}
.footer-bar a:hover {
    color: #fff;
    text-decoration: underline;
}
.footer-bar .footer-icon {
    vertical-align: middle;
    margin-right: 6px;
    font-size: 20px;
    display: inline-block;
}
@media (max-width: 600px) {
    .footer-bar { flex-direction: column; font-size: 14px; padding: 0.7rem 1vw; }
    .footer-bar .footer-center { margin: 0.3rem 0; }
}
</style>
<div class='footer-bar'>
    <div class='footer-left'>
        <span class='footer-icon'>
            <img src='https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/gmail.svg' width='22' height='22' style='filter:invert(62%) sepia(99%) saturate(7492%) hue-rotate(1deg) brightness(99%) contrast(101%); margin-right:6px; vertical-align:middle;'>
        </span>
        <a href='mailto:sayeem26s@gmail.com'>sayeem26s@gmail.com</a>
    </div>
    <div class='footer-center'>
        <span style='font-size:15px;'>Credits: <b>S.M. Shahriar</b> &mdash; All rights reserved.</span>
    </div>
    <div class='footer-right'>
        <span class='footer-icon'>
            <img src='https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg' width='22' height='22' style='filter:invert(62%) sepia(99%) saturate(7492%) hue-rotate(1deg) brightness(99%) contrast(101%); margin-right:6px; vertical-align:middle;'>
        </span>
        <a href='https://github.com/Sayeem-Velocity' target='_blank'>Sayeem-Velocity</a>
    </div>
</div>
""", unsafe_allow_html=True)
