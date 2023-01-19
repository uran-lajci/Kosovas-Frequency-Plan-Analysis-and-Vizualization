import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import streamlit as st
import re
from googletrans import Translator
import streamlit.components.v1 as components
from slider_utils import *
from filter_utils import *
from convert_values import *

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

tabForFrequencySlider, tabForFrequencyFilter, tabForStatistics, tabForAbout = st.tabs(["Frequency Slider","Frequency Filter", "Statistics", "About"])

df = pd.read_csv('FP_KOS_2022.csv')

with tabForFrequencySlider:
    st.header("Frequency allocation based on slider")

    start_clr, end_clr = st.select_slider('Select two frequencies from 1 Hz to 10 THz ',
        options=['1 Hz', '1 KHz', '10 KHz', '100 KHz', '1 MHz', '10 MHz', '100 MHz', '1 GHz', '10 GHz', '100 GHz', '1 THz', '10 THz'],
        value=('10 KHz', '1 MHz'))

    lowerBound = getLowerBoundAndFrequency(start_clr)[0]
    lowerFrequency = getLowerBoundAndFrequency(start_clr)[1]
    upperBound = getUpperBoundAndFrequency(end_clr)[0]
    upperFrequency = getUpperBoundAndFrequency(end_clr)[1]
    tabForLowerBounds, tabForUpperBounds, tabForBothBounds = st.tabs(["Lower Bound Frequencies", "Upper Bound Frequencies", "Lower and Upper Frequencies"])

    with tabForLowerBounds:
        selectedRows = df[(df["_lowerFrequency"] >= lowerBound) & (df["_lowerFrequency"] <= upperBound)]
        
        if(lowerFrequency != upperFrequency):
            st.subheader("You have selected the lower frequency records from " + lowerFrequency + " to " + upperFrequency)
        else:
            st.subheader("You have selected the lower frequency records in " + lowerFrequency)

        rowesInMHz = {}
        rowesInMHz['_lowerFrequency'] = selectedRows['_lowerFrequency'] / 10 ** 6
        rowesInMHz['_term'] = selectedRows["_term"]
        fig = px.scatter(
                rowesInMHz,
                x="_lowerFrequency",
                y="_term",
                size="_lowerFrequency",
                color="_term",
                hover_name="_term",
                log_x=True,
                size_max=60,)
        fig.update_traces(marker=dict(symbol='square'))

        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        selectedRowsWithResetedIndexes = selectedRows.reset_index(drop=True)
        newSelectedRows = []
        for i in range(len(selectedRowsWithResetedIndexes)):
            newSelectedRows.append(str(convertValues(selectedRowsWithResetedIndexes["_lowerFrequency"].loc[i])[0]) + \
                 " " + str(convertValues(selectedRowsWithResetedIndexes["_lowerFrequency"].loc[i])[1]))

        selectedRows['_lowerFrequency'] = newSelectedRows
      
        chart = alt.Chart(selectedRows).mark_square().encode(
            x='_lowerFrequency',
            y='_term',
            color='_term',
        ).interactive()
        
        st.altair_chart(chart)

    with tabForUpperBounds:
        selectedRows = df[(df["_higherFrequency"] >= lowerBound) & (df["_higherFrequency"] <= upperBound)]
        if(lowerFrequency != upperFrequency):
            st.subheader("You have selected the upper frequency records from " + lowerFrequency + " to " + upperFrequency)
        else:
            st.subheader("You have selected the upper frequency records in " + lowerFrequency)
        
        rowesInMHz = {}
        rowesInMHz['_higherFrequency'] = selectedRows['_higherFrequency'] / 10 ** 6
        rowesInMHz['_term'] = selectedRows["_term"]
        fig = px.scatter(
                rowesInMHz,
                x="_higherFrequency",
                y="_term",
                size="_higherFrequency",
                color="_term",
                hover_name="_term",
                log_x=True,
                size_max=60,)
        fig.update_traces(marker=dict(symbol='square'))
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        selectedRowsWithResetedIndexes = selectedRows.reset_index(drop=True)
        newSelectedRows = []
        for i in range(len(selectedRowsWithResetedIndexes)):
            newSelectedRows.append(str(convertValues(selectedRowsWithResetedIndexes["_lowerFrequency"].loc[i])[0]) + \
                 " " + str(convertValues(selectedRowsWithResetedIndexes["_lowerFrequency"].loc[i])[1]))

        selectedRows['_lowerFrequency'] = newSelectedRows
      
        chart = alt.Chart(selectedRows).mark_square().encode(
            x='_lowerFrequency',
            y='_term',
            color='_term',
        ).interactive()
        
        st.altair_chart(chart)

    with tabForBothBounds:
        selectedRows = df[(df["_lowerFrequency"] >= lowerBound) & (df["_higherFrequency"] <= upperBound)]
        if(lowerFrequency != upperFrequency):
            st.subheader("You have selected the records from " + lowerFrequency + " to " + upperFrequency)
        else:
            st.subheader("You have selected the frequency records in " + lowerFrequency)
        
        rowesInMHz = {}
        rowesInMHz['_lowerFrequency'] = selectedRows['_lowerFrequency'] / 10 ** 6
        rowesInMHz['_higherFrequency'] = selectedRows['_higherFrequency'] / 10 ** 6
        rowesInMHz['_term'] = selectedRows["_term"]

        fig = px.scatter(
            rowesInMHz,
            x="_lowerFrequency",
            y="_higherFrequency",
            color="_term",
            hover_name="_term",
            log_x=True,
        )
        fig.update_traces(marker=dict(symbol='square'))
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tabForFrequencyFilter:
    st.header("Frequency allocation based on filter")
    term = np.append("All", df['_term'].unique())
    
    with st.form(key='frequencyFilter'):
        col1,col2,col3, col4 = st.columns(4)
        with col1:
            frequencyBands = st.selectbox('Frequency bands',(getFrequencyBounds()))
        with col2:
            selectedTerm = st.selectbox('Term', options=list(term))
        with col3:
            selectedLanguage = st.selectbox('Language', (getLanguages()))
        with col4:
            searchType = st.radio("Status", ("primary", "secondary"))
            graphOrientation = st.radio("Graph orientation", ("Horizontal", "Vertical"))
            
        submit = st.form_submit_button(label='Search')

    if submit:
        lowerBound = getLowerBoundAndUpperBound(frequencyBands)[0]
        upperBound = getLowerBoundAndUpperBound(frequencyBands)[1]

        if(selectedTerm == "All"):
            dataset = df[
                (df['_lowerFrequency'] >= lowerBound) & 
                (df['_higherFrequency'] <= upperBound) & 
                (df['_status'] == searchType)]
        else:
            dataset = df[
                (df['_lowerFrequency'] >= lowerBound) & 
                (df['_higherFrequency'] <= upperBound) & 
                (df['_term'] == selectedTerm) & 
                (df['_status'] == searchType)]

        if(len(dataset) == 0):
            st.write("No data!")
        else:
            colors = getColors()

            graphContainer = []
            if(graphOrientation == "Horizontal"):
                with open("./css/horizontalStyles.css") as style:
                    graphContainer = [f""" </div><style>{style.read()}</style>"""]
            else:
                with open("./css/verticalStyles.css") as style:
                    graphContainer = [f""" </div> <style>{style.read()}</style>"""]

            graphContainer.append("<div class='containerSlider'>")
            datasetWithResetedIndexes = dataset.reset_index(drop=True)
            translator = Translator()
            languageAbbreviation = getAbbreviationForLanguage(selectedLanguage)

            for i in range(len(datasetWithResetedIndexes)):
                graphContainer.append(f"""
                <div style="background-color:{colors[i]};filter: invert(5);mix-blend-mode: difference;">
                    <h3>{translator.translate(datasetWithResetedIndexes["_term"].loc[i], dest=languageAbbreviation).text}</h3>
                    <p><b>
                    {convertValuesAsString(datasetWithResetedIndexes["_lowerFrequency"].loc[i])}
                     - 
                    {convertValuesAsString(datasetWithResetedIndexes["_higherFrequency"].loc[i])}                    
                    </b></p>
                </div>""")
            
            components.html("".join(graphContainer), height=200, scrolling=True)

def statistics():
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
                        freeFrequency = df[(df["_lowerFrequency"] == number*1000)]
                    elif frequencyUnit=='MHz':
                        freeFrequency = df[(df["_lowerFrequency"] == number*1000000)]
                    elif frequencyUnit=='GHz':
                        freeFrequency = df[(df["_lowerFrequency"] == number*1000000000)]
                else:
                    if frequencyUnit =='KHz':
                        freeFrequency = df[(df["_higherFrequency"] == number*1000)]
                    elif frequencyUnit=='MHz':
                        freeFrequency = df[(df["_higherFrequency"] == number*1000000)]
                    elif frequencyUnit=='GHz':
                        freeFrequency = df[(df["_higherFrequency"] == number*1000000000)]

                if len(freeFrequency)>0:
                    st.write("There are ", len(freeFrequency), " rows in this frequency")
                    datasetWithResetedIndexes = freeFrequency.reset_index(drop=True)
                    newRowsLower = []
                    for i in range(len(datasetWithResetedIndexes["_lowerFrequency"])):
                        newRowsLower.append(convertValuesAsString(datasetWithResetedIndexes["_lowerFrequency"].loc[i]))
                    
                    newRowsHigher = []
                    for i in range(len(datasetWithResetedIndexes["_higherFrequency"])):
                        newRowsHigher.append(convertValuesAsString(datasetWithResetedIndexes["_higherFrequency"].loc[i]))

                    datasetWithResetedIndexes["_lowerFrequency"] = newRowsLower
                    datasetWithResetedIndexes["_higherFrequency"] = newRowsHigher

                    st.write(datasetWithResetedIndexes.drop(['_shortComments'],axis=1))
                else:
                    st.write("This frequency is free")

    with st.form(key='statistics_groupByTerm'):
            st.subheader("Group by Frequency Term")
            term=df['_term'].unique()
            frequencyTerm = st.selectbox('Frequency Term',(term))
            submit_search = st.form_submit_button(label='Search')

            if submit_search:
                GroupByTerm = df[(df["_term"] == frequencyTerm)]
                tabTable, tabPlot= st.tabs(["table", "plot"])

                with tabTable:
                    datasetWithResetedIndexes = GroupByTerm.reset_index(drop=True)
                    newRowsLower = []
                    for i in range(len(datasetWithResetedIndexes["_lowerFrequency"])):
                        newRowsLower.append(convertValuesAsString(datasetWithResetedIndexes["_lowerFrequency"].loc[i]))
                    
                    newRowsHigher = []
                    for i in range(len(datasetWithResetedIndexes["_higherFrequency"])):
                        newRowsHigher.append(convertValuesAsString(datasetWithResetedIndexes["_higherFrequency"].loc[i]))

                    datasetWithResetedIndexes["_lowerFrequency"] = newRowsLower
                    datasetWithResetedIndexes["_higherFrequency"] = newRowsHigher

                    st.table(datasetWithResetedIndexes.drop(['_shortComments'],axis=1))
                with tabPlot:
                    rowesInMHz = {}
                    rowesInMHz['_lowerFrequency'] = GroupByTerm['_lowerFrequency'] / 10 ** 6
                    rowesInMHz['_higherFrequency'] = GroupByTerm['_higherFrequency'] / 10 ** 6
                    rowesInMHz['_status'] = GroupByTerm["_status"]
                    fig = px.scatter(
                        rowesInMHz,
                        x="_lowerFrequency",
                        y="_status",
                        size="_lowerFrequency",
                        color="_lowerFrequency",
                        hover_name="_status",
                        log_x=True,
                        size_max=60,)
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with st.form(key='statistics_groupByStatus'):
            st.subheader("Group by Frequency Status")        
            status=df['_status'].unique()
            frequencyStatus = st.selectbox('Frequency Status',(status))
            submit_search = st.form_submit_button(label='Search')

            if submit_search:
                GroupByStatus = df[(df["_status"] == frequencyStatus)]
                tabTable, tabPlot= st.tabs(["table", "plot"])

                with tabTable:
                    datasetWithResetedIndexes = GroupByStatus.reset_index(drop=True)
                    newRowsLower = []
                    for i in range(len(datasetWithResetedIndexes["_lowerFrequency"])):
                        newRowsLower.append(convertValuesAsString(datasetWithResetedIndexes["_lowerFrequency"].loc[i]))
                    
                    newRowsHigher = []
                    for i in range(len(datasetWithResetedIndexes["_higherFrequency"])):
                        newRowsHigher.append(convertValuesAsString(datasetWithResetedIndexes["_higherFrequency"].loc[i]))

                    datasetWithResetedIndexes["_lowerFrequency"] = newRowsLower
                    datasetWithResetedIndexes["_higherFrequency"] = newRowsHigher

                    st.table(datasetWithResetedIndexes.drop(['_shortComments'],axis=1))

                with tabPlot:
                    rowesInMHz = {}
                    rowesInMHz['_lowerFrequency'] = GroupByStatus['_lowerFrequency'] / 10 ** 6
                    rowesInMHz['_higherFrequency'] = GroupByStatus['_higherFrequency'] / 10 ** 6
                    rowesInMHz['_term'] = GroupByStatus["_term"]
                    fig = px.scatter(
                        rowesInMHz,
                        x="_lowerFrequency",
                        y="_term",
                        size="_lowerFrequency",
                        color="_term",
                        hover_name="_higherFrequency",
                        log_x=True,
                        size_max=60,)
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tabForStatistics:
    st.header("Statistics for experts") 
            
    login, signup = st.tabs(["Login", "Signup"])

    def check_word_in_file(file_path, word):
        with open(file_path, 'r') as file:
            file_contents = file.read()
            if re.search(word, file_contents):
                return True
        return False

    with login:
        login_successful = False
        st.title("Login Form")

        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        
        if not all([username,password]):
            st.error("Username and password are required fields.")
        else:
            file_path = 'usernames_and_passwords.txt'
            if check_word_in_file(file_path, username + ", Password:") and check_word_in_file(file_path, ": " + password):
                login_successful = True
            else:
                login_successful = False

        if login_successful:
            st.success("Welcome, {}!".format(username))
            statistics()
        else:
            st.error("Invalid username or password.")

    with signup:
        def handle_signup():
            username = st.text_input("Username", key="rusername")
            password = st.text_input("Password", type="password", key="rpassword")
            password_confirm = st.text_input("Confirm Password", type="password", key="password_confirm")
            if st.button("Sign up"):
                if not all([username,password,password_confirm]):
                    st.error("All fields are required.")
                elif password != password_confirm:
                    st.error("Passwords do not match.")
                else:
                    file_path = 'usernames_and_passwords.txt'

                    if check_word_in_file(file_path, username) and check_word_in_file(file_path, password):
                        signup_successful = False
                    else:
                        signup_successful = True

                    if signup_successful:
                        with open("usernames_and_passwords.txt", "a") as f:
                            f.write("\nUsername: {}, Password: {}".format(username, password))
                        st.success("Account created for {}!".format(username))
                    else:
                        st.error("Sorry, there was a problem creating the account.")

        st.title("Signup Form")
        handle_signup()
        
with tabForAbout:
   st.header("About")
   st.subheader("Përshkrimi i projektit")
   st.markdown('Ky projekt është zhvilluar në kuadër të Universitetit të Prishtinës të nivelit master departmenti Inxhinieri Kompjuterike për digjitalizim të sherbimeve të ARKEP: Vizualizimi interaktiv ne Ueb i te dhenave te planit frekuencor. Të dhënat janë marrë nga ARKEP dhe janë shfytëzuar gjatë zhvillimit dhe testimit të programit.')
   st.markdown("Ky projekt është zhvilluar në gjuhën programuese Python dhe janë përdorur libraritë Streamlit, Pandas, numpy,ploty.express, seaborn, matplotlib për vizualizim dhe googletrans për përkthim.")
   st.markdown("https://streamlit.io/")
   st.markdown("https://docs.python.org/3/")
   st.markdown("https://numpy.org/doc/")
   st.markdown("https://plotly.com/python/plotly-express/")
   st.markdown("https://seaborn.pydata.org/")
   st.markdown("https://matplotlib.org/stable/index.html")
   st.markdown("https://py-googletrans.readthedocs.io/en/latest/")
   st.markdown("Aplikacionet ne te cilat jami bazur jane:")
   st.markdown("http://tablice.hakom.hr:8080/vis?lang=hr")
   st.markdown("https://efis.cept.org/include2/graphTool.jsp?lowRange=10000+kHz&highRange=50000+kHz&action=search&specifyRange=1&low=10000&high=50000&unit=kHz&user=54&languages=Albanian&searchOption=Allocation&compare=on&orientation=vertical")
   st.subheader('Përshkrimi i datasetit')
   st.markdown('Dataseti që kemi përdorur në këtë projket është shpërndarja dhe aplikimi i radio-frekuencave në Republikën e Kosovës që i takojn brezit nga 8.3KHz deri në 3000GHz, i cili na është dhënë nga ARKEP. Ky dataset përmban frekuencën e ulët, frekuencën e lart, statusin dhe llojin e frekunecës, dhe përmban rreth 1431 të dhëna.')
   st.subheader("Ky projekt është zhvilluar nga:")
   st.markdown("Elvir Misini -- elvir.misini@student.uni-pr.edu")
   st.markdown("Uran Lajçi -- uran.lajci@student.uni-pr.edu")