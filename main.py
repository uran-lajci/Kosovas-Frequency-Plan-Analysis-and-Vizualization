import pandas as pd
import numpy as np
import plotly.express as px
import time
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from googletrans import Translator

st.set_page_config(layout="wide")

tab1, tab2, tab3, tab7 = st.tabs(["Frequency Slider","Frequency Filter", "Statistics", "About"])

df = pd.read_csv('frequency.csv')

with tab1:
    

    st.header("Frequency allocation based on slider")
    lower= df["Lower Frequency"].min()
    higher= df["Lower Frequency"].max()

    start_clr, end_clr = st.slider("Select a range of frequences",
                        value=(int(lower), int(higher)))

    selectedRows = df[(df["Lower Frequency"] >= start_clr) & (df["Higher Frequency"] <= end_clr)]
    st.write("You have selected ", len(selectedRows), " rows")
    tab4, tab5,tab6= st.tabs(["table","bar", "plot"])
    with tab4:
        st.write(selectedRows)
#    field=df['Field'].unique()

    with tab5:
        st.bar_chart(data=selectedRows, x='Lower Frequency', y='Field', width=0, height=0, use_container_width=True)

    with tab6:
        fig = px.scatter(
            selectedRows,
            x="Lower Frequency",
            y="Field",
            size="Lower Frequency",
            color="Location",
            hover_name="Location",
            log_x=True,
            size_max=60,
        )

        st.plotly_chart(fig, theme="streamlit", use_container_width=True)



with tab2:
    st.header("Frequency allocation based on filter")
    location = df['Location'].unique()
    field=df['Field'].unique()

    translator = Translator()

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
            languageFromDataset = st.selectbox('Language', (
                'Bangla',
                'English',
                'Koren',
                'French',
                'German',
                'Hebrew',
                'Hindi',
                'Italian',
                'Japanese',
                'Latin',
                'Malay',
                'Nepali',
                'Russian',
                'Arabic',
                'Chinese',
                'Spanish'
            ))
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

        if languageFromDataset == 'Bangla':
            lang = 'bn'
        elif languageFromDataset == 'English':
            lang = 'en'
        elif languageFromDataset == 'Koren':
            lang = 'ko'
        elif languageFromDataset == 'German':
            lang = 'de'
        elif languageFromDataset == 'Hebrew':
            lang = 'he'
        elif languageFromDataset == 'Hindi':
            lang = 'hi'
        elif languageFromDataset == 'Italian':
            lang = 'it'
        elif languageFromDataset == 'Japanese':
            lang = 'ja'
        elif languageFromDataset == 'Latin':
            lang = 'la'
        elif languageFromDataset == 'Malay':
            lang = 'ms'
        elif languageFromDataset == 'Nepali':
            lang = 'ne'
        elif languageFromDataset == 'Russian':
            lang = 'ru'
        elif languageFromDataset == 'Arabic':
            lang = 'ar'
        elif languageFromDataset == 'Chinese':
            lang = 'zh'
        elif languageFromDataset == 'Spanish':
            lang = 'es'
        
        
        dataset = df[(df['Lower Frequency'] >= lowerBound) & (df['Lower Frequency'] <= upperBound) 
            & (df['Location'] == state) & (df['Type'] == searchType)]
        
        dataset['Location'] = dataset['Location'].apply(translator.translate, dest=lang).apply(getattr, args=('text',))
        dataset['Type'] = dataset['Type'].apply(translator.translate, dest=lang).apply(getattr, args=('text',))
        dataset['Field'] = dataset['Field'].apply(translator.translate, dest=lang).apply(getattr, args=('text',))
        dataset['Status'] = dataset['Status'].apply(translator.translate, dest=lang).apply(getattr, args=('text',))
        st.write(dataset)

        

        # st.bar_chart(data=dataset, x='Lower Frequency', y='Field', width=0, height=0, use_container_width=True)

        # fig = px.scatter(
        #     dataset,
        #     x="Lower Frequency",
        #     y="Field",
        #     size="Lower Frequency",
        #     color="Location",
        #     hover_name="Location",
        #     log_x=True,
        #     size_max=60,
        # )
        # st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab3:
   st.header("Statistics for experts")
with tab7:
   st.header("About")
   st.markdown('Ky projekt është zhvilluar në kuadër të Universitetit të Prishtinës të nivelit master departmenti **Inxhinieri Kompjuterike** për digjitalizim të sherbimeve të ARKEP: Vizualizimi interaktiv ne Ueb i te dhenave te planit frekuencor. Të dhënat janë marrë nga ARKEP dhe janë shfytëzuar gjatë zhvillimit dhe testimit të programit.')
   st.markdown("Ky projekt është zhvilluar në gjuhën programuese :red[Python] dhe është përdorur libraria **:blue[Streamlit]** për vizualizim.")
   st.markdown("https://streamlit.io/")
   st.markdown("https://docs.python.org/3/")
   st.markdown("Ky projekt është zhvilluar nga:")
   st.markdown("Elvir Misini -- elvir.misini@student.uni-pr.edu")
   st.markdown("Uran Lajçi -- uran.lajci@student.uni-pr.edu")

   #st.image("https://static.streamlit.io/examples/owl.jpg", width=200)