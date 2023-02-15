from utils.slider_utils import *
from utils.filter_utils import *
from utils.general_utils import *

import streamlit as st
import plotly.express as px
import altair as alt

def getBounds(df, start_slider, end_slider, frequency):
    lower_bound, lower_frequency = getLowerBoundAndFrequency(start_slider)
    upper_bound, upper_frequency = getUpperBoundAndFrequency(end_slider)
    selected_rows = df[(df[frequency] >= lower_bound) & (df[frequency] <= upper_bound)]

    if lower_frequency != upper_frequency:
        st.subheader(f"You have selected the upper frequency records from {lower_frequency} to {upper_frequency}")
    else:
        st.subheader(f"You have selected the upper frequency records in {lower_frequency}")

    selected_rows_mhz = selected_rows.copy()
    selected_rows_mhz[frequency] = selected_rows_mhz[frequency] / 10 ** 6

    generate_charts(selected_rows_mhz, frequency)

def generate_charts(selected_rows, frequency):
    fig = px.scatter(
        selected_rows,
        x=frequency,
        y="service",
        size=frequency,
        color="service",
        hover_name="service",
        log_x=True,
        size_max=60,)
    fig.update_traces(marker=dict(symbol='square'))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    selected_rows_with_reset_indexes = selected_rows.reset_index(drop=True)
    new_selected_rows = []

    for i in range(len(selected_rows_with_reset_indexes)):
        new_selected_rows.append(str(convertValues(selected_rows_with_reset_indexes["_higherFrequency"].loc[i])[0]) + " " + str(convertValues(selected_rows_with_reset_indexes["_higherFrequency"].loc[i])[1]))

    selected_rows['_higherFrequency'] = new_selected_rows

    chart = alt.Chart(selected_rows).mark_square().encode(
        x='_higherFrequency',
        y='service',
        color='service',
    ).interactive()

    st.altair_chart(chart)

def getBothBounds(df, start_slider, end_slider):
    lower_bound, lower_frequency = getLowerBoundAndFrequency(start_slider)
    upper_bound, upper_frequency = getUpperBoundAndFrequency(end_slider)
    filtered_df = df[(df["_lowerFrequency"] >= lower_bound) & (df["_higherFrequency"] <= upper_bound)]
    st.subheader("You have selected the frequency records from {} to {}".format(lower_frequency, upper_frequency))
    
    frequencies_in_MHz = {
        '_lowerFrequency': filtered_df['_lowerFrequency'] / 10 ** 6,
        '_higherFrequency': filtered_df['_higherFrequency'] / 10 ** 6,
        'service': filtered_df["service"]
    }
    fig = px.scatter(
        frequencies_in_MHz,
        x="_lowerFrequency",
        y="_higherFrequency",
        color="service",
        hover_name="service",
        log_x=True,
    )
    fig.update_traces(marker=dict(symbol='square'))
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

def getFrequencySlider(df):
    st.header("Frequency allocation based on slider")

    start_slider, end_slider = st.select_slider(
        'Select two frequencies from 1 Hz to 10 THz ',
        options=['1 Hz', '1 KHz', '10 KHz', '100 KHz', '1 MHz', '10 MHz', '100 MHz', '1 GHz', '10 GHz', '100 GHz', '1 THz', '10 THz'],
        value=('10 KHz', '1 MHz'))
    tabForLowerBounds, tabForUpperBounds, tabForBothBounds = st.tabs(["Lower Bound Frequencies", "Upper Bound Frequencies", "Lower and Upper Frequencies"])

    with tabForLowerBounds:
        getBounds(df, start_slider, end_slider, "_lowerFrequency")
    with tabForUpperBounds:
        getBounds(df, start_slider, end_slider, "_higherFrequency")
    with tabForBothBounds:
        getBothBounds(df, start_slider, end_slider)