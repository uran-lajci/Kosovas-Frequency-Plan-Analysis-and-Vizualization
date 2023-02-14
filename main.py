from main_functions.slider_utils import *
from main_functions.convert_values import *
from main_functions.frequency_slider import *
from main_functions.frequency_filter import *
from main_functions.statistics import *
from main_functions.about import *

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

tabForFrequencySlider, tabForFrequencyFilter, tabForStatistics, tabForAbout = st.tabs(["Frequency Slider", "Frequency Filter", "Statistics", "About"])

dataset = pd.read_csv('FP_KOS_2022.csv')
dataset = dataset.rename(columns={'_term': 'service'})

with tabForFrequencySlider:
    getFrequencySlider(dataset)

with tabForFrequencyFilter:
    getFrequencyFilter(dataset)

with tabForStatistics:
    getStatistics(dataset)

with tabForAbout:
    getAbout()