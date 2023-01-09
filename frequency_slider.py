import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv('FP_KOS_2022.csv')

st.header("Frequency allocation based on slider")
st.write("1 Hz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp; 100 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 100 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 100 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 THz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 THz")
start_clr, end_clr = st.slider("Select a range of Frequencies",value=(0, 110), step=10, label_visibility="hidden")

if(start_clr == 0):
    lowerBound = 0
    lowerFrequency = "1 Hz"
elif(start_clr == 10):
    lowerBound = 10 ** 3
    lowerFrequency = "1 KHz"
elif(start_clr == 20):
    lowerBound = 10 ** 4
    lowerFrequency = "10 KHz"
elif(start_clr == 30):
    lowerBound = 10 ** 5
    lowerFrequency = "100 KHz"
elif(start_clr == 40):
    lowerBound = 10 ** 6
    lowerFrequency = "1 MHz"
elif(start_clr == 50):
    lowerBound = 10 ** 7
    lowerFrequency = "10 MHz"
elif(start_clr == 60):
    lowerBound = 10 ** 8
    lowerFrequency = "100 MHz"
elif(start_clr == 70):
    lowerBound = 10 ** 9
    lowerFrequency = "1 GHz"
elif(start_clr == 80):
    lowerBound = 10 ** 10
    lowerFrequency = "10 GHz"
elif(start_clr == 90):
    lowerBound = 10 ** 11
    lowerFrequency = "100 GHz"
elif(start_clr == 100):
    lowerBound = 10 ** 12
    lowerFrequency = "1 THz"
elif(start_clr == 110):
    lowerBound = 10 ** 13
    lowerFrequency = "10 THz"

if(end_clr == 0):
    upperBound = 0
    upperFrequency = "1 Hz"
elif(end_clr == 10):
    upperBound = 10 ** 3
    upperFrequency = "1 KHz"
elif(end_clr == 20):
    upperBound = 10 ** 4
    upperFrequency = "10 KHz"
elif(end_clr == 30):
    upperBound = 10 ** 5
    upperFrequency = "100 KHz"
elif(end_clr == 40):
    upperBound = 10 ** 6
    upperFrequency = "1 MHz"
elif(end_clr == 50):
    upperBound = 10 ** 7
    upperFrequency = "10 MHz"
elif(end_clr == 60):
    upperBound = 10 ** 8
    upperFrequency = "100 MHz"
elif(end_clr == 70):
    upperBound = 10 ** 9
    upperFrequency = "1 GHz"
elif(end_clr == 80):
    upperBound = 10 ** 10
    upperFrequency = "10 GHz"
elif(end_clr == 90):
    upperBound = 10 ** 11
    upperFrequency = "100 GHz"
elif(end_clr == 100):
    upperBound = 10 ** 12
    upperFrequency = "1 THz"
elif(end_clr == 110):
    upperBound = 10 ** 13
    upperFrequency = "10 THz"

tabForLowerBounds, tabForUpperBounds = st.tabs(["Lower Bound Frequencies", "Upper Bound Frequencies"])

with tabForLowerBounds:
    selectedRows = df[(df["_lowerFrequency"] >= lowerBound) & (df["_lowerFrequency"] <= upperBound)]
    if(lowerFrequency != upperFrequency):
        st.subheader("You have selected the lower frequency records from " + lowerFrequency + " to " + upperFrequency)
    else:
        st.subheader("You have selected the lower frequency records in " + lowerFrequency)
    
    fig = px.scatter(
            selectedRows,
            x="_lowerFrequency",
            y="_term",
            size="_lowerFrequency",
            color="_term",
            hover_name="_term",
            log_x=True,
            size_max=60,
        )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    st.bar_chart(data=selectedRows, x='_term', y='_lowerFrequency', width=0, height=0, use_container_width=True)

with tabForUpperBounds:
    selectedRows = df[(df["_higherFrequency"] >= lowerBound) & (df["_higherFrequency"] <= upperBound)]
    if(lowerFrequency != upperFrequency):
        st.subheader("You have selected the upper frequency records from " + lowerFrequency + " to " + upperFrequency)
    else:
        st.subheader("You have selected the upper frequency records in " + lowerFrequency)
    
    fig = px.scatter(
            selectedRows,
            x="_higherFrequency",
            y="_term",
            size="_higherFrequency",
            color="_term",
            hover_name="_term",
            log_x=True,
            size_max=60,
        )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    st.bar_chart(data=selectedRows, x='_term', y='_higherFrequency', width=0, height=0, use_container_width=True)
    


