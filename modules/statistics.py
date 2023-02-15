from utils.slider_utils import *
from utils.filter_utils import *
from utils.general_utils import *
from authentication.login import *
from authentication.signup import *

import streamlit as st
import plotly.express as px

def getFreeFrequencyTab(dataset):
    st.subheader("Search if a specific frequency is free!")
    col1, col2 = st.columns(2)
    with col1:
        search_frequency = st.number_input('Insert a frequency')
    with col2:
        frequency_scale = st.selectbox('Frequency Units', (
            'KHz',
            'MHz',
            'GHz',
        ))
    submit_search = st.form_submit_button(label='Search')

    if submit_search:
        search_frequency_hz = convertToHz(search_frequency, frequency_scale)
        free_frequency = dataset[(dataset["_lowerFrequency"] <= search_frequency_hz) & (dataset["_higherFrequency"] >= search_frequency_hz)]

        if len(free_frequency) > 0:
            st.write(f"There are {len(free_frequency)} rows in this frequency")
            st.write(free_frequency.to_string(index=False))
        else:
            st.write("This frequency is free")

def getGroupedBy(dataset, group_by_col, frequency_col):
    st.subheader(f"Group by Frequency {group_by_col.capitalize()}")
    unique_group_by = dataset[group_by_col].unique()
    frequency_group_by = st.selectbox(f'Frequency {group_by_col.capitalize()}', unique_group_by)
    submit_search = st.form_submit_button(label='Search')

    if submit_search:
        group_by_freq = dataset[dataset[group_by_col] == frequency_group_by]
        tabTable, tabPlot = st.tabs(["table", "plot"])

        with tabTable:
            dataset_with_reseted_indexes = group_by_freq.reset_index(drop=True)
            dataset_with_reseted_indexes["_lowerFrequency"] = [convertFrequencyToString(val) for val in dataset_with_reseted_indexes["_lowerFrequency"]]
            dataset_with_reseted_indexes["_higherFrequency"] = [convertFrequencyToString(val) for val in dataset_with_reseted_indexes["_higherFrequency"]]
            st.table(dataset_with_reseted_indexes.drop(['_shortComments'], axis=1))

        with tabPlot:
            fig = px.scatter(
                group_by_freq,
                x="_lowerFrequency",
                y=frequency_col,
                size="_lowerFrequency",
                color=frequency_col,
                hover_name="_higherFrequency",
                log_x=True,
                size_max=60,
            )
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    
def getStatistics(dataset):
    st.header("Statistics for experts")
    login, signup = st.tabs(["Login", "Signup"])

    with login:
        if isLogedIn() == True:
            with st.form(key='statistics'):
                getFreeFrequencyTab(dataset)
            with st.form(key='statistics_groupByTerm'):
                getGroupedBy(dataset, "service", "_status")
            with st.form(key='statistics_groupByStatus'):                
                getGroupedBy(dataset, "_status", "service")
    with signup:
        getSignup()