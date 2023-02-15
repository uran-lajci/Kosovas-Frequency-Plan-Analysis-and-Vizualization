from utils.slider_utils import *
from utils.general_utils import *
from modules.frequency_slider import *
from modules.frequency_filter import *
from modules.statistics import *
from modules.about import *

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

dataset = pd.read_csv('FP_KOS_2022.csv')
dataset = dataset.rename(columns={'_term': 'service'})

tabForFrequencySlider, tabForFrequencyFilter, tabForStatistics, tabForAbout = st.tabs(["Frequency Slider", "Frequency Filter", "Statistics", "About"])
with tabForFrequencySlider:
    getFrequencySlider(dataset)

with tabForFrequencyFilter:
    getFrequencyFilter(dataset)

with tabForStatistics:
    getStatistics(dataset)

with tabForAbout:
    getAbout()