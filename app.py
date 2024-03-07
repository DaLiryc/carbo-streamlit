import streamlit as st
import requests
import pandas as pd
import numpy as np
import datetime

#If api in the cloud please update the url with the url
url = 'https://cabotrack-qoz5nlx2ga-ew.a.run.app'

st.markdown("# This is our version of the Carbotrack app! #")
    
    
'''
Please be aware that our app and our models are still at an early stage and can lack accuracy or not be able to detect food type!

**DO NOT** use as a medical guidance, always follow recomendations from your doctor!

Please upload/take a picture and test our app and see how much dose of insuline you should take based on the picture of your food received!
'''
uploaded_file = st.file_uploader('Photo of your meal', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False, help='Upload your photo')

if uploaded_file is not None:
    col1, col2, col3 = st.columns([1,2,1])  # Create columns for layout
    with col2:  # Display the uploaded image in the middle column
        st.image(uploaded_file, width=340)
        
col1, col2, col3 = st.columns([1,2,1])  # Create columns for layout
      
with col2:  # Put the button in the middle column
    col2_1, col2_2, col2_3 = st.columns([1,4,1])  # Create sub-columns within col2
    with col2_2:  # Put the button in the middle sub-column
        if st.button("Let's try to detect food type and give you an insuline recomendation!", key='predict'):
            if uploaded_file is not None:
                files = {'image': uploaded_file}
                with st.spinner('Trying to detect food type and give you an insuline recomendation!'):
                    response = requests.post(url + '/predict', files=files)
                if response.status_code == 200:
                    st.write("Here are the results: ", response.json())
                else:
                    st.write("Food not yet recognized, our model is still learning, sorry!")
            else:
                st.write("Please upload an image")