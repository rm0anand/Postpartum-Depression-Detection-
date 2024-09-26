import streamlit as st
from streamlit_option_menu import option_menu
import pickle

import warnings
import pandas as pd
from io import StringIO
import requests




prediction_model = pickle.load(open("stacking_clf.sav", "rb"))

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

    
    # Feature mapping
    # Mapping for 'age'//
    age_mapping = {'25-30': 0, '30-35': 1, '35-40': 2, '40-45': 3, '45-50': 4}

    # Mapping for 'irritable_towards_baby_and_partner'//
    irritable_towards_baby_and_partner_mapping = {'Yes': 2, 'No': 0, 'Sometimes': 1}

    # Mapping for 'trouble_sleeping_at_night'//
    trouble_sleeping_at_night_mapping = {'Two or more days a week': 1, 'No': 0, 'Yes': 2}

    # Mapping for 'problems_concentrating_or_making_decision'//
    problems_concentrating_or_making_decision_mapping = {'Yes': 2, 'No': 0, 'Often': 1}

    # Mapping for 'overeating_or_loss_of_appetite'//
    overeating_or_loss_of_appetite_mapping = {'Yes': 2, 'No': 0, 'Not at all': 1}

    # Mapping for 'problems_of_bonding_with_baby'//
    problems_of_bonding_with_baby_mapping = {'Yes': 2, 'Sometimes': 1, 'No': 0}

    # Mapping for 'suicide_attempt'//
    suicide_mapping = {'Yes': 2, 'No': 0, 'Not interested to say': 1}

    # Mapping for 'feeling_of_guilt'//
    feeling_of_guilt_mapping = {'No': 1, 'Yes': 2, 'Maybe': 0}

    # Mapping for 'feeling_sad_or_tearful'//
    feeling_sad_or_tearful_mapping = {'Yes': 2, 'No': 0, 'Sometimes': 1}




    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.selectbox(label='Age of the Person', options=list(age_mapping.keys()))
        
    with col2:  
        problems_of_bonding_with_baby = st.selectbox(label='Problems of bonding with baby',options=list(problems_of_bonding_with_baby_mapping.keys()))
    
    with col3:
        problems_concentrating_or_making_decision = st.selectbox(label='Problems Concentrating or Making Decision', options=list(problems_concentrating_or_making_decision_mapping.keys()))
    
    with col1:
        irritable_towards_baby_and_partner = st.selectbox(label='Irritable towards baby and partner', options=list(irritable_towards_baby_and_partner_mapping.keys()))

    with col2:
        suicide_attempt= st.selectbox(label= 'Suicide Attempt', options=list(suicide_mapping.keys()))
        
    with col3:
        feeling_of_guilt = st.selectbox(label= "Feeling guilty", options=list(feeling_of_guilt_mapping.keys()))
    
    with col1:
        feeling_sad_or_tearful= st.selectbox(label= "Feeling Sad or Tearful?", options = list(feeling_sad_or_tearful_mapping.keys()))

    with col2:
        overeating_or_loss_of_appetite = st.selectbox(label= "Over eating or Loss of Appetite", options = list(overeating_or_loss_of_appetite_mapping.keys()))

    with col3:
        trouble_sleeping_at_night = st.selectbox(label = "trouble_sleeping_at_night", options= list(trouble_sleeping_at_night_mapping.keys()))



        age = age_mapping[age]
        problems_concentrating_or_making_decision= problems_concentrating_or_making_decision_mapping[problems_concentrating_or_making_decision]
        problems_of_bonding_with_baby = problems_of_bonding_with_baby_mapping[problems_of_bonding_with_baby]
        irritable_towards_baby_and_partner = irritable_towards_baby_and_partner_mapping[irritable_towards_baby_and_partner]
        suicide_attempt = suicide_mapping[suicide_attempt]
        feeling_of_guilt = feeling_of_guilt_mapping[feeling_of_guilt]
        feeling_sad_or_tearful = feeling_sad_or_tearful_mapping[feeling_sad_or_tearful]
        overeating_or_loss_of_appetite = overeating_or_loss_of_appetite_mapping[overeating_or_loss_of_appetite]
        trouble_sleeping_at_night = trouble_sleeping_at_night_mapping[trouble_sleeping_at_night]

    
    riskLevel=""
    predicted_risk = [0] 
    # creating a button for Prediction
    with col1:
        if st.button('Predict Maternal Mental Health'):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                predicted_risk = prediction_model.predict([[age,feeling_sad_or_tearful,irritable_towards_baby_and_partner,trouble_sleeping_at_night,problems_concentrating_or_making_decision,overeating_or_loss_of_appetite,problems_of_bonding_with_baby,suicide_attempt,feeling_of_guilt]])

            # st
            st.subheader("Risk Level:")
            if predicted_risk[0] == 0:
                st.markdown('<bold><p style="font-weight: bold; font-size: 20px; color: green;">Low Risk</p></bold>', unsafe_allow_html=True)
            else: 
                st.markdown('<bold><p style="font-weight: bold; font-size: 20px; color: red;">High Risk</p><bold>', unsafe_allow_html=True)
    with col2:
        if st.button("Clear"): 
            st.rerun()
