import joblib
import pandas as pd
import streamlit as st

# load model and feature names
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

st.title("Chiller Pump Fault Detection")
st.write("Enter the sensor readings for the two chiller pumps.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Chiller Pump 1")
    chp1_temp1 = st.number_input("Temperature 1 (Deg C)", value=39.5, key="chp1_t1")
    chp1_temp2 = st.number_input("Temperature 2 (Deg C)", value=39.0, key="chp1_t2")
    chp1_vib1 = st.number_input("Vibration 1 (mm/s)", value=1.30, format="%.3f", key="chp1_v1")
    chp1_vib2 = st.number_input("Vibration 2 (mm/s)", value=1.80, format="%.3f", key="chp1_v2")

with col2:
    st.subheader("Chiller Pump 2")
    chp2_temp1 = st.number_input("Temperature 1 (Deg C)", value=39.3, key="chp2_t1")
    chp2_temp2 = st.number_input("Temperature 2 (Deg C)", value=40.5, key="chp2_t2")
    chp2_vib1 = st.number_input("Vibration 1 (mm/s)", value=1.50, format="%.3f", key="chp2_v1")
    chp2_vib2 = st.number_input("Vibration 2 (mm/s)", value=2.90, format="%.3f", key="chp2_v2")

if st.button("Predict"):
    # same column order as in training
    values = [chp1_temp1, chp1_temp2, chp2_temp1, chp2_temp2,
              chp1_vib1, chp1_vib2, chp2_vib1, chp2_vib2]
    data = pd.DataFrame([values], columns=features)

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.error(f"Fault detected (fault probability: {probability:.2f})")
    else:
        st.success(f"Normal condition (fault probability: {probability:.2f})")
