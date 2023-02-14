from main_functions.slider_utils import *
from main_functions.filter_utils import *
from main_functions.convert_values import *

import numpy as np
import streamlit as st
from googletrans import Translator
import streamlit.components.v1 as components

def getFrequencyFilter(dataset):
    st.header("Frequency allocation based on filter")
    term = np.append("All", dataset['service'].unique())

    with st.form(key='frequencyFilter'):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            frequency_bands = st.selectbox('Frequency bands', (getFrequencyBounds()))
        with col2:
            selected_term = st.selectbox('Service', options=list(term))
        with col3:
            selected_language = st.selectbox('Language', (getLanguages()))
        with col4:
            search_type = st.radio("Status", ("primary", "secondary", "all"))
            graph_orientation = st.radio("Graph orientation", ("Horizontal", "Vertical"))

        submit = st.form_submit_button(label='Search')

    if submit:
        lower_bound = getLowerBoundAndUpperBound(frequency_bands)[0]
        upper_bound = getLowerBoundAndUpperBound(frequency_bands)[1]

        if selected_term == "All":
            if search_type == 'all':
                dataset = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                             (dataset['_higherFrequency'] <= upper_bound)]
            else:        
                dataset = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                             (dataset['_higherFrequency'] <= upper_bound) & 
                             (dataset['_status'] == search_type)]
        else:
            if search_type == 'all':
                dataset = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                             (dataset['_higherFrequency'] <= upper_bound) & 
                             (dataset['service'] == selected_term)]  
            else:  
                dataset = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                             (dataset['_higherFrequency'] <= upper_bound) & 
                             (dataset['service'] == selected_term) & 
                             (dataset['_status'] == search_type)]

        if len(dataset) == 0:
            st.write("No data!")
        else:
            st.write("There are ", len(dataset), " rows in this frequency")
                    
            colors = getColors()

            graph_container = []
            if graph_orientation == "Horizontal":
                with open("./css/horizontalStyles.css") as style:
                    graph_container = [f""" </div><style>{style.read()}</style>"""]
            else:
                with open("./css/verticalStyles.css") as style:
                    graph_container = [f""" </div> <style>{style.read()}</style>"""]

            graph_container.append("<div class='containerSlider'>")
            dataset_with_reseted_indexes = dataset.reset_index(drop=True)
            translator = Translator()
            language_abbreviation = getAbbreviationForLanguage(selected_language)

            for i in range(len(dataset_with_reseted_indexes)):
                graph_container.append(f"""
                <div style="background-color:{colors[i]};filter: invert(5);mix-blend-mode: difference;">
                    <h3>{translator.translate(dataset_with_reseted_indexes["service"].loc[i], dest=language_abbreviation).text}</h3>
                    <p><b>
                    {convertValuesAsString(dataset_with_reseted_indexes["_lowerFrequency"].loc[i])}
                     - 
                    {convertValuesAsString(dataset_with_reseted_indexes["_higherFrequency"].loc[i])}                    
                    </b></p>
                </div>""")
            
            components.html("".join(graph_container), height=200, scrolling=True)