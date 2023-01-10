import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from googletrans import Translator
import translators as ts
import streamlit.components.v1 as components
from slider_bound_and_frequency import *
from filter_utils import *

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

tab1, tab2, tab3, tab7 = st.tabs(["Frequency Slider","Frequency Filter", "Statistics", "About"])

df = pd.read_csv('FP_KOS_2022.csv')

with tab1:
    st.header("Frequency allocation based on slider")
    st.write("1 Hz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp; 100 KHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 100 MHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 100 GHz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 1 THz &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 10 THz")
    start_clr, end_clr = st.slider("Select a range of Frequencies",value=(0, 110), step=10, label_visibility="hidden")

    lowerBound = getLowerBoundAndFrequency(start_clr)[0]
    lowerFrequency = getLowerBoundAndFrequency(start_clr)[1]
    upperBound = getUpperBoundAndFrequency(end_clr)[0]
    upperFrequency = getUpperBoundAndFrequency(end_clr)[1]

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

with tab2:
    st.header("Frequency allocation based on filter")
    dummy = []
    dummy = np.append(dummy,"All")
    term = np.append(dummy, df['_term'].unique())
    
    with st.form(key='salaryform'):
        col1,col2,col3, col4 = st.columns(4)
        with col1:
            frequencyBands = st.selectbox('Frequency bands',(getFrequencyBounds()))
        with col2:
            state = st.selectbox('Term', options=list(term))
        with col3:
            languageFromDataset = st.selectbox('Language', (getLanguages()))
        with col4:
            searchType = st.radio("Status", ("primary", "secondary"))
            allocationOrientation = st.radio("Allocation orientation", ("Horizontal", "Vertical"))
            
        submit_salary = st.form_submit_button(label='Search')

    if submit_salary:
        lowerBound = getLowerBoundAndUpperBound(frequencyBands)[0]
        upperBound = getLowerBoundAndUpperBound(frequencyBands)[1]

        lang = getAbbreviationForLanguage(languageFromDataset)
        
        if(state == "All"):
            dataset = df[(df['_lowerFrequency'] >= lowerBound) & (df['_lowerFrequency'] <= upperBound) 
                & (df['_status'] == searchType)]
        else:
            dataset = df[(df['_lowerFrequency'] >= lowerBound) & (df['_lowerFrequency'] <= upperBound) 
                & (df['_term'] == state) & (df['_status'] == searchType)]
    
        if(len(dataset) == 0):
            st.write("No data!")
        else:
        
            colors = getColors()

            html_string = []
            if(allocationOrientation == "Horizontal"):
                html_string = [""" 
                    </div>
                    <style>
                    .ccc123 {
                        width: 100%;
                        overflow-x: auto;
                        white-space: nowrap;
                    }
                    .ccc123 div {
                        width:200px;
                        height:150px;
                        display:inline-block;
                        line-height:2.5;
                        padding:20px;
                    }
                    </style>
                """
                ]
            else:
                html_string = [""" 
                    </div>
                    <style>
                    .ccc123 {
                        height: 100%;
                        display: flex;
                        padding-bottom: 100px;
                        margin-bottom: 100px;
                        flex-wrap: wrap;
                        align-content: center;
                        flex-direction: row;
                    }
                    .ccc123 > div {
                        width:200px;
                        height:150px;
                        display:inline-block;
                        line-height:2.5;
                        padding:20px;
                    }
                    </style>
                """
                ]

            html_string.append("<div class='ccc123'>")

            df2 = dataset.reset_index(drop=True)
            translator = Translator()
            for i in range(len(df2)):
                html_string.append(
                    f"""
                <div style="background-color:{colors[i]};">
                    <h5>{translator.translate(df2["_term"].loc[i], dest=lang).text}</h5>
                    <p>{df2["_lowerFrequency"].loc[i]} Hz - {df2["_higherFrequency"].loc[i]} Hz</p>
                </div>
                """
                )
            
            components.html("".join(html_string), height=200, scrolling=True)  # JavaScript works
    
with tab3:
   st.header("Statistics for experts")
   df_test = pd.read_csv('FP_KOS_2022.csv')
   with st.form(key='statistics'):
        st.subheader("Search if a specific frequency is free!")
        col1,col2,col3 = st.columns(3)
        
        with col1:
           number = st.number_input('Insert a number')  
        with col2:
            frequencyUnit = st.selectbox('Frequency Units',(
                'KHz',
                'MHz',
                'GHz',))
        
        with col3:
            frequency = st.selectbox('Higher/lower',(
                'Lower Frequency',
                'Higher Frequency',))
        
        submit_search = st.form_submit_button(label='Search')

        freeFrequency=[]
        if submit_search:
            if frequency=='Lower Frequency':
                if frequencyUnit =='KHz':
                    freeFrequency = df_test[(df_test["_lowerFrequency"] == number*1000)]
                elif frequencyUnit=='MHz':
                    freeFrequency = df_test[(df_test["_lowerFrequency"] == number*1000000)]
                elif frequencyUnit=='GHz':
                    freeFrequency = df_test[(df_test["_lowerFrequency"] == number*1000000000)]
            else:
                if frequencyUnit =='KHz':
                    freeFrequency = df_test[(df_test["_higherFrequency"] == number*1000)]
                elif frequencyUnit=='MHz':
                    freeFrequency = df_test[(df_test["_higherFrequency"] == number*1000000)]
                elif frequencyUnit=='GHz':
                    freeFrequency = df_test[(df_test["_higherFrequency"] == number*1000000000)]

            if len(freeFrequency)>0:
                st.write("There are ", len(freeFrequency), " rows in this frequency")
                st.write(freeFrequency.drop(['_shortComments'],axis=1))
            else:
                st.write("This frequency is **:green[free]**")
        
####################################################

   with st.form(key='statistics_groupByTerm'):
        st.subheader("Group by Frequency Term")
        
        
        term=df_test['_term'].unique()
        frequencyTerm = st.selectbox('Frequency Term',(term))
        
        submit_search = st.form_submit_button(label='Search')
        if submit_search:
            GroupByTerm = df_test[(df_test["_term"] == frequencyTerm)]
            

            tabTable, tabPlot= st.tabs(["table", "plot"])
            with tabTable:
                st.write(GroupByTerm.drop(['_shortComments'],axis=1))
            
            with tabPlot:
                fig = px.scatter(
                    GroupByTerm,
                    x="_lowerFrequency",
                    y="_status",
                    size="_lowerFrequency",
                    color="_lowerFrequency",
                    hover_name="_status",
                    log_x=True,
                    size_max=60,
                )

                st.plotly_chart(fig, theme="streamlit", use_container_width=True)


#########################################
   with st.form(key='statistics_groupByStatus'):
        st.subheader("Group by Frequency Status")
        df_test = pd.read_csv('FP_KOS_2022.csv')
        
        status=df_test['_status'].unique()
        frequencyStatus = st.selectbox('Frequency Status',(status))
        
        submit_search = st.form_submit_button(label='Search')

        if submit_search:
            GroupByStatus = df_test[(df_test["_status"] == frequencyStatus)]

            tabTable, tabPlot= st.tabs(["table", "plot"])
            with tabTable:
                st.write(GroupByStatus.drop(['_shortComments'],axis=1))
            
            with tabPlot:
                fig = px.scatter(
                    GroupByStatus,
                    x="_lowerFrequency",
                    y="_term",
                    size="_lowerFrequency",
                    color="_term",
                    hover_name="_higherFrequency",
                    log_x=True,
                    size_max=60,
                )

                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        

           # st.write(GroupByStatus)
        


    
with tab7:
   st.header("About")
   st.subheader("Përshkrimi i projektit")
   st.markdown('Ky projekt është zhvilluar në kuadër të Universitetit të Prishtinës të nivelit master departmenti **Inxhinieri Kompjuterike** për digjitalizim të sherbimeve të ARKEP: Vizualizimi interaktiv ne Ueb i te dhenave te planit frekuencor. Të dhënat janë marrë nga ARKEP dhe janë shfytëzuar gjatë zhvillimit dhe testimit të programit.')
   st.markdown("Ky projekt është zhvilluar në gjuhën programuese :red[Python] dhe janë përdorur libraritë **:blue[Streamlit]**, **:blue[Pandas]**, **:blue[numpy]**,**:blue[ploty.express]**, **:blue[seaborn]**, **:blue[matplotlib]** për vizualizim dhe **:blue[googletrans] për përkthim**.")
   st.markdown("https://streamlit.io/")
   st.markdown("https://docs.python.org/3/")
   st.markdown("https://numpy.org/doc/")
   st.markdown("https://plotly.com/python/plotly-express/")
   st.markdown("https://seaborn.pydata.org/")
   st.markdown("https://matplotlib.org/stable/index.html")
   st.markdown("https://py-googletrans.readthedocs.io/en/latest/")
   st.subheader('Përshkrimi i datasetit')
   st.markdown('Dataseti që kemi përdorur në këtë projket është shpërndarja dhe aplikimi i radio-frekuencave në Republikën e Kosovës që i takojn brezit nga 8.3KHz deri në 3000GHz, i cili na është dhënë nga ARKEP. Ky dataset përmban frekuencën e ulët, frekuencën e lart, statusin dhe llojin e frekunecës, dhe përmban rreth 1431 të dhëna.')
   st.subheader("Ky projekt është zhvilluar nga:")
   st.markdown("Elvir Misini -- elvir.misini@student.uni-pr.edu")
   st.markdown("Uran Lajçi -- uran.lajci@student.uni-pr.edu")