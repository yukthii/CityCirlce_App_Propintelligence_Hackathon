# 🏙️ CityCircle – AI-Powered Smart City Decision Support System

CityCircle is a **people-first smart city platform** that leverages **AI-driven analytics and computer vision** to enable **preventive and data-driven urban decision-making**.  
The system integrates **citizen activity data** and **road accident image analysis** into a **single interactive dashboard**.

---

## 🚀 Problem Statement

Smart cities generate vast amounts of data, but city authorities often lack **simple, unified tools** to convert this data into **actionable insights**.  
Citizen health risks, sustainability concerns, and road accident alerts are handled in **separate systems**, leading to delayed and reactive responses.

---

## 💡 Solution Overview

CityCircle provides a **unified AI-powered dashboard** that:

- Analyzes citizen lifestyle and sustainability data to determine **risk levels**
- Detects road accidents from CCTV images using **computer vision techniques**
- Supports **manual real-time inputs** for live scenario testing
- Presents insights through a **clean and interactive interface**

The platform is designed to be **modular, scalable, and real-time ready**.

---

## 🧠 Key Features

### 👥 Citizen Risk Analysis
- Uses citizen activity data (steps walked, sleep hours, carbon footprint)
- Generates **Low / Medium / High risk** classifications
- Supports **manual input** for real-time risk prediction

### 🚦 Road Accident Detection
- Analyzes CCTV images using **image-based heuristics**
- Detects **Accident / No Accident**
- Displays **confidence score (%)**
- Allows **manual image upload**

### 📊 Interactive Dashboard
- Built using **Streamlit**
- Visual risk distribution charts
- Accident alert image gallery
- User-friendly and responsive layout

---

## 🏗️ System Architecture

**Architecture Layers:**
1. **UI Layer** – Streamlit dashboard & Figma UI design  
2. **Data Layer** – Citizen activity CSV dataset & CCTV image samples  
3. **AI Processing Layer** –  
   - Rule-based citizen risk scoring  
   - Computer vision–based accident detection  
4. **Decision Layer** – Alerts, insights, and visual analytics  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- OpenCV  
- Pillow  
- Google Colab  
- Figma  

---

## 📂 Project Structure

CityCircle/
│
├── app.py
├── citizen_risk_analysis_output.csv
├── accident_detection_output.csv
├── accident_images/
│   ├── accident/
│   └── non_accident/
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

pip install streamlit pandas pillow opencv-python
2️⃣ Run the Application
streamlit run app.py

## 🎯 Demo Capabilities

View city-wide citizen risk distribution

Enter manual inputs to test AI predictions

Upload CCTV images to simulate accident detection

Observe confidence-based AI output

## 🔮 Future Scope

Real-time CCTV feed integration

Deep learning–based accident detection

City-level heatmaps and predictive analytics

Emergency response system integration

Multilingual citizen interfaces

## 🏆 Hackathon Note

This project was developed as a rapid prototype for a hackathon.
Rule-based AI and heuristic computer vision techniques were used to ensure fast, explainable, and scalable implementation within limited development time.

👩‍💻 Team

### Developed by Team Yukthi
Team Members:
Jyothi RK
Kavya M
Kavyashree K
Margaret Sheela C

### Theme: Smart Cities & Infrastructure

📌 One-Line Summary

CityCircle transforms smart city data into actionable insights using AI-driven analytics and computer vision, enabling preventive and people-first urban decision-making.
