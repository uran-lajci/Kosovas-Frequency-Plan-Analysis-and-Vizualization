import pandas as pd
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")
st.title("Titulli - Frequency")
df = pd.read_csv('C:\\Users\\uran_\\frequenct_data.csv')


with st.form(key='salaryform'):
    col1,col2,col3, col4 = st.columns(4)
    
    with col1:
        option1 = st.selectbox('Frequency bands',(
            '3 - 30 kHz',
            '30 - 300 kHz',
            '300 kHz - 3 MHz',
            '3 - 30 MHz',
            '30 MHz - 300 MHz',
            '300 MHz - 3 GHz',
            '3 - 30 GHz',
            '30 - 300 GHz'))
    with col2:
        option2 = st.selectbox('Frequency table',(
            'Albania',
            'Austria',
            'Belgium',
            'Croatia',
            'France',
            'Germany',
            'Greece',
            'Portugal'))
    with col3:
        option3 = st.selectbox('Language',(
            'Albanian',
            'Bosnian',
            'Croation',
            'English',
            'German',
            'Greek',
            'Portugal'))
    with col4:
        searchType = st.radio("Search Type", ("Application", "Alocation"))
        check = st.checkbox("Compare (Select multiple frequency tables)")
        allocationOrientation = st.radio("Allocation orientation", ("Horizontal", "Vertical"))
        
    submit_salary = st.form_submit_button(label='Search')

if submit_salary:
    st.write(option1)
    st.write(option2)
    st.write(option3)
    st.write(searchType)
    st.write(check)
    st.write(allocationOrientation)

    

