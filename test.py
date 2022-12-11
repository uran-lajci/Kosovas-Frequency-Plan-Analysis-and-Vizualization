import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\uran_\Downloads\frequenct_data (1).csv")

def replace_values(column, initial, final):
    dataset[column] = dataset[column].replace(initial, final)

frequency_dict = {
    '5A': 174.928, 
    '7D': 194.064, 
    '8A': 195.936, 
    '8C': 197.648, 
    '9A': 202.928,
    '9B': 204.64,
    '9C': 206.352,
    '10A':209.936,
    '10B':211.648,
    '10C':213.36,
    '10D':215.072,
    '11A':216.928,
    '11B':218.64,
    '11C':220.352,
    '11D':222.064,
    '12A':223.936,
    '12B':225.648,
    '12C':227.36,
    '12D':229.072
}

for key, value in frequency_dict.items():
    replace_values('Frequency', key, value)

dataset['Frequency'] = pd.to_numeric(dataset['Frequency'], downcast="float")
dataset["Inclusion"] = pd.to_datetime(dataset["Inclusion"], infer_datetime_format=True)
dataset["Modification"] = pd.to_datetime(dataset["Modification"], infer_datetime_format=True)
dataset["Expiration"] = pd.to_datetime(dataset["Expiration"], infer_datetime_format=True)

dataset['Inclusion'] = dataset['Inclusion'].fillna(dataset['Inclusion'].mean())
dataset['Modification'] = dataset['Modification'].fillna(dataset['Modification'].mean())
dataset['Expiration'] = dataset['Expiration'].fillna(dataset['Expiration'].mean())
dataset['Range'] = dataset['Range'].fillna("Less than 3000001")
dataset['Restrictions'] = dataset['Restrictions'].fillna("unknown")

frequecyLevels = [0,80,90,100,110,104.90,250]
start_clr, end_clr = st.select_slider("Select a range of frequences", options=frequecyLevels,
                    value=(0, 250))

selectedRows = dataset[(dataset["Frequency"] >= start_clr) & (dataset["Frequency"] <= end_clr)]
st.write("You have selected ", len(selectedRows), " rows")
st.write(selectedRows)


first = dataset.loc[(dataset['Frequency'] >= 0) & (dataset['Frequency'] < 90)]
fig1, ax = plt.subplots()
first.groupby('User')['Frequency'].plot(style='.-', legend=True)
ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
st.pyplot(fig1)

second = dataset.loc[(dataset['Frequency'] >= 91) & (dataset['Frequency'] < 100)]
fig2, ax = plt.subplots()
second.groupby('User')['Frequency'].plot(style='.-', legend=True)
ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
st.pyplot(fig2)

third = dataset.loc[(dataset['Frequency'] >= 101) & (dataset['Frequency'] < 110)]
fig3, ax = plt.subplots()
third.groupby('User')['Frequency'].plot(style='.-', legend=True)
ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
st.pyplot(fig3)

fourth = dataset.loc[(dataset['Frequency'] >= 111)]
fig4, ax = plt.subplots()
fourth.groupby('User')['Frequency'].plot(style='.-', legend=True)
ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
st.pyplot(fig4)