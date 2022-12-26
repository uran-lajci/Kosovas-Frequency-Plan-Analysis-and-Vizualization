import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tab1, tab2, tab3 = st.tabs(["Frequency Slider", "Frequency From Filter", "About"])
##python -m streamlit run da
with tab1:
    st.header("Frequency allocation based on slider")
    df = pd.read_csv(r"C:\Users\Elvir Misini\Downloads\frequency.csv")

    lower=df["Lower Frequency"].min()
    higher=df["Lower Frequency"].max()

    start_clr, end_clr = st.slider("Select a range of frequences",
                        value=(int(lower), int(higher)))

    selectedRows = df[(df["Lower Frequency"] >= start_clr) & (df["Higher Frequency"] <= end_clr)]
    st.write("You have selected ", len(selectedRows), " rows")
    st.write(selectedRows)

with tab2:
  st.header("Frequency allocation based on filter")

  location = df['Location'].unique()
  language = df['Language'].unique()

  with st.form(key='salaryform'):
    col1,col2,col3, col4 = st.columns(4)
    
    with col1:
        frequencyBands = st.selectbox('Frequency bands',(
            '3 - 30 kHz',
            '30 - 300 kHz',
            '300 kHz - 3 MHz',
            '3 - 30 MHz',
            '30 MHz - 300 MHz',
            '300 MHz - 3 GHz',
            '3 - 30 GHz',
            '30 - 300 GHz'))
    with col2:
        state = st.selectbox('Frequency table', options=list(location))
    with col3:
        languageFromDataset = st.selectbox('Language', options=list(language))
    with col4:
        searchType = st.radio("Search Type", ("Application", "Alocation"))
        check = st.checkbox("Compare (Select multiple frequency tables)")
        allocationOrientation = st.radio("Allocation orientation", ("Horizontal", "Vertical"))
        
    submit_salary = st.form_submit_button(label='Search')

    if submit_salary:
        if frequencyBands == "3 - 30 kHz":
            lowerBound = 3
            upperBound = 30
        elif frequencyBands == "30 - 300 kHz":
            lowerBound = 30
            upperBound = 300
        elif frequencyBands == "300 kHz - 3 MHz":
            lowerBound = 300
            upperBound = 30000
        elif frequencyBands == "3 - 30 MHz":
         lowerBound = 30000 
         upperBound = 300000 
        elif frequencyBands == "30 MHz - 300 MHz":
            lowerBound = 300000 
            upperBound = 3000000 
        elif frequencyBands == "300 MHz - 3 GHz":
            lowerBound = 300000
            upperBound = 3000000
        elif frequencyBands == "3 - 30 GHz":
            lowerBound = 3000000
            upperBound = 30000000
        elif frequencyBands == "'30 - 300 GHz'":
            lowerBound = 30000000
            upperBound = 300000000
            
        st.write(df[(df['Lower Frequency'] >= lowerBound) & (df['Lower Frequency'] <= upperBound) 
            & (df['Location'] == state)
            & (df['Language'] == languageFromDataset)
            & (df['Type'] == searchType)    
        ])
        st.write(check)
        st.write(allocationOrientation)
    
with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)