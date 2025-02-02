import streamlit as st
import pickle
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

# Load the models and encoder
with open('liver_disease_prediction.pkl', 'rb') as f:
    liver_model = pickle.load(f)

with open('kidney_disease_prediction.pkl', 'rb') as f:
    kidney_model = pickle.load(f)

with open('Parkinson_disease_prediction.pkl', 'rb') as f:
    parkinsons_model = pickle.load(f)

with open('encoder_kidney_diseases.pkl', 'rb') as f:
    kidney_encoder = pickle.load(f)

# Display the image at the top of the page without the 'key' argument
st.image('Multiple Diseases Prediction.jpg', use_container_width=True)

# Streamlit App
st.title("Disease Prediction App")

# Navigation Menu
disease = option_menu(
    menu_title="Select a Disease to Predict", 
    options=["Liver Disease", "Kidney Disease", "Parkinson's Disease"],
    icons=["droplet", "activity", "brain"],
    menu_icon="hospital",
    default_index=0,
    orientation="horizontal"
)

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

if disease == "Liver Disease":
    st.subheader("Liver Disease Prediction")
    age = st.text_input("Age")
    total_bilirubin = st.text_input("Total Bilirubin")
    alkaline_phosphotase = st.text_input("Alkaline Phosphotase")
    alanine_aminotransferase = st.text_input("Alanine Aminotransferase")
    albumin = st.text_input("Albumin")
    
    if st.button("Predict"):
        features = [safe_float(age), safe_float(total_bilirubin), safe_float(alkaline_phosphotase), safe_float(alanine_aminotransferase), safe_float(albumin)]
        if None in features:
            st.error("Please enter valid numerical values for all fields.")
        else:
            prediction = liver_model.predict([features])
            result = "Likely to have Liver Disease" if prediction[0] == 1 else "Not likely to have Liver Disease"
            st.write("Prediction:", result)

elif disease == "Kidney Disease":
    st.subheader("Kidney Disease Prediction")
    sg = st.text_input("Specific Gravity")
    al = st.text_input("Albumin")
    pc = st.text_input("Pus Cell")
    bgr = st.text_input("Blood Glucose Random")
    bu = st.text_input("Blood Urea")
    sod = st.text_input("Sodium")
    hemo = st.text_input("Hemoglobin")
    pcv = st.text_input("Packed Cell Volume")
    rc = st.text_input("Red Blood Cell Count")
    htn = st.text_input("Hypertension (1 for Yes, 0 for No)")
    dm = st.text_input("Diabetes Mellitus (1 for Yes, 0 for No)")
    appet = st.text_input("Appetite (1 for Good, 0 for Poor)")
    pe = st.text_input("Pedal Edema (1 for Yes, 0 for No)")
    ane = st.text_input("Anemia (1 for Yes, 0 for No)")
    
    if st.button("Predict"):
        features = [safe_float(sg), safe_float(al), safe_float(pc), safe_float(bgr), safe_float(bu), safe_float(sod), safe_float(hemo), safe_float(pcv), safe_float(rc), safe_int(htn), safe_int(dm), safe_int(appet), safe_int(pe), safe_int(ane)]
        if None in features:
            st.error("Please enter valid numerical values for all fields.")
        else:
            encoded_features = np.array(features).reshape(1, -1)  # Ensure proper reshaping
            prediction = kidney_model.predict(encoded_features)
            result = "Likely to have Kidney Disease" if prediction[0] == 1 else "Not likely to have Kidney Disease"
            st.write("Prediction:", result)

elif disease == "Parkinson's Disease":
    st.subheader("Parkinson's Disease Prediction")
    fo = st.text_input("MDVP:Fo(Hz)")
    flo = st.text_input("MDVP:Flo(Hz)")
    jitter_abs = st.text_input("MDVP:Jitter(Abs)")
    shimmer = st.text_input("MDVP:Shimmer")
    shimmer_db = st.text_input("MDVP:Shimmer(dB)")
    apq3 = st.text_input("Shimmer:APQ3")
    apq5 = st.text_input("Shimmer:APQ5")
    mdvp_apq = st.text_input("MDVP:APQ")
    shimmer_dda = st.text_input("Shimmer:DDA")
    hnr = st.text_input("HNR")
    rpde = st.text_input("RPDE")
    spread1 = st.text_input("Spread1")
    spread2 = st.text_input("Spread2")
    d2 = st.text_input("D2")
    ppe = st.text_input("PPE")
    
    if st.button("Predict"):
        features = [safe_float(fo), safe_float(flo), safe_float(jitter_abs), safe_float(shimmer), safe_float(shimmer_db), safe_float(apq3), safe_float(apq5), safe_float(mdvp_apq), safe_float(shimmer_dda), safe_float(hnr), safe_float(rpde), safe_float(spread1), safe_float(spread2), safe_float(d2), safe_float(ppe)]
        if None in features:
            st.error("Please enter valid numerical values for all fields.")
        else:
            prediction = parkinsons_model.predict([features])
            result = "Likely to have Parkinson's Disease" if prediction[0] == 1 else "Not likely to have Parkinson's Disease"
            st.write("Prediction:", result)
