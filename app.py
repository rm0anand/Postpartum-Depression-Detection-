import streamlit as st
from streamlit_option_menu import option_menu
import pickle

import warnings
import pandas as pd
from io import StringIO
import requests


prediction_model = pickle.load(open('C:\\Users\\Anand\\Desktop\\ppdd_steamlit\\stacking_clf.sav', "rb"))

#sidebar navigavation
with st.sidebar:
    st.title("PostPartum Wellness")
    st.write("Get Predictive Insights of your mental health")
    # st.write("")

    selected = option_menu('Postpartum Wellness',
                           ['About us',
                            'Mental health predictor','dashboard'],
                            icons=[]
                           )
    
if (selected == 'About us'):
    
    st.title("Welcome to Mental Health Predictor")
    st.write("At Mental Health Predictor, Our goal is to change the way healthcare is delivered by providing innovative solutions using predictive analysis. "
         "Our platform has been specifically constructed to tackle the complicated aspects of post pregnancy health, giving precise information "
        )
    
    col1, col2= st.columns(2)
    with col1:
        # Section 1: Pregnancy Risk Prediction
        st.header("1.Mental Health Prediction")
        st.write("this mental health Prediction feature utilizes sophisticated algorithms to analyze different parameters, like age, "
                " By processing this information, we provide accurate predictions of "
                "potential risks during postpartum depression.")
        # Add an image for Pregnancy Risk Prediction
        st.image("https://www.simplypsychology.org/wp-content/uploads/postpartum-depression.jpeg", caption="mental health Prediction", use_column_width=True)
      
    # Closing note
    st.write("Thank you for choosing us.We are dedicated to improving healthcare by using technology and predictive analytics."
            "Please take a look at our features and take advantage of the insights we offer.")    
    
if (selected== 'Mental health predictor'):
    st.title('Mental Health Predictor')
    content = "Predicting postpartum mental health important for new mothers and babies"
    st.markdown(f"<div style='white-space: pre-wrap;'><b>{content}</b></div></br>", unsafe_allow_html=True)

    age_mapping = {'25-30': 0, '30-35': 1, '35-40': 2, '40-45': 3, '45-50': 4}
    bonding_mapping= {'No': 0, 'Sometimes': 1, 'Yes': 2}
    concentration_mapping = {'No': 0, 'Often': 1, 'Yes': 2}
    irritability_mapping ={'No': 0, 'Sometimes': 1, 'Yes': 2}
    suicide_mapping = {'No':0,'Yes':2,'Not interested to say':1}

    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.selectbox(label='Age of the Person', options=list(age_mapping.keys()))
        
    with col2:  
        problems_of_bonding_with_baby = st.selectbox(label='Problems of bonding with baby',options=list(bonding_mapping.keys()))
    
    with col3:
        problems_concentrating_or_making_decision = st.selectbox(label='Problems Concentrating or Making Decision', options=list(concentration_mapping.keys()))
    
    with col1:
        irritable_towards_baby_and_partner = st.selectbox(label='Irritable towards baby and partner', options=list(irritability_mapping.keys()))

    with col2:
        suicide_attempt= st.selectbox(label= 'Suicide Attempt', options=list(suicide_mapping.keys()))
        
        age = age_mapping[age]
        problems_concentrating_or_making_decision= concentration_mapping[problems_concentrating_or_making_decision]
        problems_of_bonding_with_baby = bonding_mapping[problems_of_bonding_with_baby]
        irritable_towards_baby_and_partner = irritability_mapping[irritable_towards_baby_and_partner]
        suicide_attempt = suicide_mapping[suicide_attempt]
    
    riskLevel=""
    predicted_risk = [0] 
    # creating a button for Prediction
    with col1:
        if st.button('Predict Maternal Mental Health'):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                predicted_risk = prediction_model.predict([[problems_of_bonding_with_baby, problems_concentrating_or_making_decision, age, irritable_towards_baby_and_partner, suicide_attempt]])

            # st
            st.subheader("Risk Level:")
            if predicted_risk[0] == 0:
                st.markdown('<bold><p style="font-weight: bold; font-size: 20px; color: green;">Low Risk</p></bold>', unsafe_allow_html=True)
            else: 
                st.markdown('<bold><p style="font-weight: bold; font-size: 20px; color: red;">High Risk</p><bold>', unsafe_allow_html=True)
    with col2:
        if st.button("Clear"): 
            st.rerun()
