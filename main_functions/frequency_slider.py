from main_functions.slider_utils import *
from main_functions.filter_utils import *
from main_functions.convert_values import *

import streamlit as st
import plotly.express as px
import altair as alt

def getFrequencySlider(df):
    st.header("Frequency allocation based on slider")

    start_slider, end_slider = st.select_slider(
        'Select two frequencies from 1 Hz to 10 THz ',
        options=['1 Hz', '1 KHz', '10 KHz', '100 KHz', '1 MHz', '10 MHz', '100 MHz', '1 GHz', '10 GHz', '100 GHz', '1 THz', '10 THz'],
        value=('10 KHz', '1 MHz'))

    lower_bound, lower_frequency = getLowerBoundAndFrequency(start_slider)
    upper_bound, upper_frequency = getUpperBoundAndFrequency(end_slider)

    tabForLowerBounds, tabForUpperBounds, tabForBothBounds = st.tabs(["Lower Bound Frequencies", "Upper Bound Frequencies", "Lower and Upper Frequencies"])

    with tabForLowerBounds:
        selected_rows = df[(df["_lowerFrequency"] >= lower_bound) & (df["_lowerFrequency"] <= upper_bound)]
        if(lower_frequency != upper_frequency):
            st.subheader("You have selected the lower frequency records from " + lower_frequency + " to " + upper_frequency)
        else:
            st.subheader("You have selected the lower frequency records in " + lower_frequency)

        rowes_in_MHz = {}
        rowes_in_MHz['_lowerFrequency'] = selected_rows['_lowerFrequency'] / 10 ** 6
        rowes_in_MHz['service'] = selected_rows["service"]
        fig = px.scatter(
                rowes_in_MHz,
                x="_lowerFrequency",
                y="service",
                size="_lowerFrequency",
                color="service",
                hover_name="service",
                log_x=True,
                size_max=60,)
        fig.update_traces(marker=dict(symbol='square'))
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        selected_rows_with_reseted_indexes = selected_rows.reset_index(drop=True)
        new_selected_rows = []
        for i in range(len(selected_rows_with_reseted_indexes)):
            new_selected_rows.append(str(convertValues(selected_rows_with_reseted_indexes["_lowerFrequency"].loc[i])[0]) + " " + str(convertValues(selected_rows_with_reseted_indexes["_lowerFrequency"].loc[i])[1]))

        selected_rows['_lowerFrequency'] = new_selected_rows

        chart = alt.Chart(selected_rows).mark_square().encode(
            x='_lowerFrequency',
            y='service',
            color='service',
        ).interactive()

        st.altair_chart(chart)

    with tabForUpperBounds:
        selected_rows = df[(df["_higherFrequency"] >= lower_bound) & (df["_higherFrequency"] <= upper_bound)]
        if(lower_frequency != upper_frequency):
            st.subheader("You have selected the upper frequency records from " + lower_frequency + " to " + upper_frequency)
        else:
            st.subheader("You have selected the upper frequency records in " + lower_frequency)

        rowes_in_MHz = {}
        rowes_in_MHz['_higherFrequency'] = selected_rows['_higherFrequency'] / 10 ** 6
        rowes_in_MHz['service'] = selected_rows["service"]
        fig = px.scatter(
                rowes_in_MHz,
                x="_higherFrequency",
                y="service",
                size="_higherFrequency",
                color="service",
                hover_name="service",
                log_x=True,
                size_max=60,)
        fig.update_traces(marker=dict(symbol='square'))
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        selected_rows_with_reset_indexes = selected_rows.reset_index(drop=True)
        new_selected_rows = []

        for i in range(len(selected_rows_with_reset_indexes)):
            new_selected_rows.append(str(convertValues(selected_rows_with_reset_indexes["_lowerFrequency"].loc[i])[0]) + " " + str(convertValues(selected_rows_with_reset_indexes["_lowerFrequency"].loc[i])[1]))

        selected_rows['_lowerFrequency'] = new_selected_rows

        chart = alt.Chart(selected_rows).mark_square().encode(
            x='_lowerFrequency',
            y='service',
            color='service',
        ).interactive()

        st.altair_chart(chart)

    with tabForBothBounds:
        selected_rows = df[(df["_lowerFrequency"] >= lower_bound) & (df["_higherFrequency"] <= upper_bound)]
        
        if(lower_frequency != upper_frequency):
            st.subheader("You have selected the records from " + lower_frequency + " to " + upper_frequency)
        else:
            st.subheader("You have selected the frequency records in " + lower_frequency)
        
        rows_in_MHz = {}
        rows_in_MHz['_lowerFrequency'] = selected_rows['_lowerFrequency'] / 10 ** 6
        rows_in_MHz['_higherFrequency'] = selected_rows['_higherFrequency'] / 10 ** 6
        rows_in_MHz['service'] = selected_rows["service"]

        fig = px.scatter(
            rows_in_MHz,
            x="_lowerFrequency",
            y="_higherFrequency",
            color="service",
            hover_name="service",
            log_x=True,
        )
        fig.update_traces(marker=dict(symbol='square'))
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)