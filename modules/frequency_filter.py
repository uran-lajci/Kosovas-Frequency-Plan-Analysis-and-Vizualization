from utils.filter_utils import *
from utils.general_utils import *

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
        lower_bound, upper_bound = getLowerBoundAndUpperBound(frequency_bands)

        if selected_term == "All":
            if search_type == 'all':
                dataset_filtered = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                                           (dataset['_higherFrequency'] <= upper_bound)]
            else:        
                dataset_filtered = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                                           (dataset['_higherFrequency'] <= upper_bound) & 
                                           (dataset['_status'] == search_type)]
        else:
            if search_type == 'all':
                dataset_filtered = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                                           (dataset['_higherFrequency'] <= upper_bound) & 
                                           (dataset['service'] == selected_term)]  
            else:  
                dataset_filtered = dataset[(dataset['_lowerFrequency'] >= lower_bound) & 
                                           (dataset['_higherFrequency'] <= upper_bound) & 
                                           (dataset['service'] == selected_term) & 
                                           (dataset['_status'] == search_type)]

        if len(dataset_filtered) == 0:
            st.write("No data!")
        else:
            st.write("There are ", len(dataset_filtered), " rows in this frequency")
            colors = getColors()
            graph_container = []
            if graph_orientation == "Horizontal":
                with open("./css/horizontal_styles.css") as style:
                    graph_container = [f""" </div><style>{style.read()}</style>"""]
            else:
                with open("./css/vertical_styles.css") as style:
                    graph_container = [f""" </div> <style>{style.read()}</style>"""]

            graph_container.append("<div class='containerSlider'>")
            dataset_filtered = dataset_filtered.reset_index(drop=True)
            translator = Translator()
            language_abbreviation = getAbbreviationForLanguage(selected_language)

            for i in range(len(dataset_filtered)):
                service_name = dataset_filtered["service"].loc[i]
                lower_frequency = convertValuesAsString(dataset_filtered["_lowerFrequency"].loc[i])
                higher_frequency = convertValuesAsString(dataset_filtered["_higherFrequency"].loc[i])
                service_name_translated = translator.translate(service_name, dest=language_abbreviation).text

                graph_container.append(f"""
                <div style="background-color:{colors[i]};filter: invert(5);mix-blend-mode: difference;">
                    <h3>{service_name_translated}</h3>
                    <p><b>{lower_frequency} - {higher_frequency}</b></p>
                </div>""")
            
            graph_container.append("</div>")
            components.html("".join(graph_container), height=200, scrolling=True)
