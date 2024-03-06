import streamlit as st
import requests
import pandas as pd
import numpy as np
import datetime

#If api in the cloud please update the url with the url
url = 'http://127.0.0.1:8000'

st.markdown("# This is our version of the Carbotrack app! #")
    
    
'''
Please be aware that our app and our models are still at an early stage and can lack accuracy or not be able to detect food type!

**DO NOT** use as a medical guidance, always follow recomendations from your doctor!

Please upload/take a picture and test our app and see how much dose of insuline you should take based on the picture of your food received!
'''
st.file_uploader('Photo of your meal', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False, help='Upload your photo')
