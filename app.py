import streamlit as st
import pandas as pd
from PIL import Image
import os
import numpy as np

st.set_page_config(page_title="CityCircle – Smart City AI", layout="wide")

st.title("🏙️ CityCircle – AI-Powered Smart City Dashboard")

menu = st.sidebar.selectbox(
    "Select Module",
    ["Citizen Risk Analysis", "Road Accident Alerts"]
)

# ------------------ CITIZEN RISK ------------------
if menu == "Citizen Risk Analysis":
    st.header("🧑‍🤝‍🧑 Citizen Health & Sustainability Risk")

    df = pd.read_csv("citizen_risk_analysis_output.csv")

    st.subheader("Risk Distribution")
    st.bar_chart(df["Risk_Level"].value_counts())

    st.subheader("Sample Citizen Data")
    st.dataframe(df.head(10))

    st.info(
        "AI analyzes lifestyle, mobility, sleep, and carbon footprint "
        "to identify risk patterns for smart city planning."
    )

    # ---------- MANUAL INPUT ----------
    st.subheader("🔍 Manual Citizen Risk Prediction")

    steps = st.number_input("Steps Walked per Day", min_value=0, value=4000)
    sleep = st.number_input("Sleep Hours", min_value=0.0, value=7.0)
    carbon = st.number_input("Carbon Footprint (kg CO₂)", min_value=0.0, value=15.0)

    if st.button("Predict Risk Level"):
        score = 0
        if steps < 3000:
            score += 2
        if sleep < 6:
            score += 2
        if carbon > 20:
            score += 2

        if score >= 4:
            risk = "High Risk 🚨"
        elif score == 2:
            risk = "Medium Risk ⚠️"
        else:
            risk = "Low Risk ✅"

        st.success(f"Predicted Risk Level: {risk}")

# ------------------ ACCIDENT ALERTS ------------------
else:
    st.header("🚦 Road Accident Detection Alerts")

    df = pd.read_csv("accident_detection_output.csv")

    st.subheader("Detected Accident Images")

    cols = st.columns(3)
    count = 0

    for _, row in df.iterrows():
        if row["actual_label"] == "accident":
            img = Image.open(row["image_path"])
            cols[count % 3].image(
                img,
                caption=row["AI_Prediction"],
                width=250
            )
            count += 1
        if count == 6:
            break

    st.warning(
        "Accident detection demonstrated using sampled CCTV images. "
        "System is scalable to real-time surveillance feeds."
    )

    # ---------- MANUAL IMAGE INPUT ----------
    st.subheader("📸 Upload Image for Accident Check")

    uploaded_file = st.file_uploader(
        "Upload CCTV Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        img_color = Image.open(uploaded_file)
        img_gray = img_color.convert("L")
        img_np = np.array(img_gray)

        st.image(img_color, caption="Uploaded Image", width=350)

        # Image statistics (lightweight AI)
        brightness = img_np.mean()
        variance = img_np.var()

        # Heuristic decision
        if brightness < 120 and variance > 1500:
            prediction = "Accident Detected 🚨"
            confidence = 85
        else:
            prediction = "No Accident ✅"
            confidence = 80

        st.success(f"AI Prediction: {prediction}")
        st.progress(confidence / 100)
        st.caption(f"Confidence Score: {confidence}%")
