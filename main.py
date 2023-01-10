import pandas as pd
import numpy as np
import plotly.express as px
import time
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from googletrans import Translator
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

tab1, tab2, tab3, tab7 = st.tabs(["Frequency Slider","Frequency Filter", "Statistics", "About"])

df = pd.read_csv('FP_KOS_2022.csv')

with tab1:
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

with tab2:
    st.header("Frequency allocation based on filter")
    dummy = []
    dummy = np.append(dummy,"All")
    term = np.append(dummy, df['_term'].unique())
    
    translator = Translator()
    with st.form(key='salaryform'):
        col1,col2,col3, col4 = st.columns(4)
        with col1:
            frequencyBands = st.selectbox('Frequency bands',(
                '3 - 30 kHz',
                '30 - 300 kHz',
                '300 kHz - 3 MHz',
                '3 - 30 MHz',
                '30 MHz - 300 MHz',
                '300 MHz - 3 GHz',
                '3 - 30 GHz',
                '30 - 300 GHz'))
        with col2:
            state = st.selectbox('Term', options=list(term))
        with col3:
            languageFromDataset = st.selectbox('Language', (
                'Bangla',
                'English',
                'Koren',
                'French',
                'German',
                'Hebrew',
                'Hindi',
                'Italian',
                'Japanese',
                'Latin',
                'Malay',
                'Nepali',
                'Russian',
                'Arabic',
                'Chinese',
                'Spanish'
            ))
        with col4:
            searchType = st.radio("Status", ("primary", "secondary"))
            allocationOrientation = st.radio("Allocation orientation", ("Horizontal", "Vertical"))
            
        submit_salary = st.form_submit_button(label='Search')

    if submit_salary:
        if frequencyBands == "3 - 30 kHz":
            lowerBound = 3
            upperBound = 30
        elif frequencyBands == "30 - 300 kHz":
            lowerBound = 30
            upperBound = 300
        elif frequencyBands == "300 kHz - 3 MHz":
            lowerBound = 300
            upperBound = 30000
        elif frequencyBands == "3 - 30 MHz":
            lowerBound = 30000 
            upperBound = 300000 
        elif frequencyBands == "30 MHz - 300 MHz":
            lowerBound = 300000 
            upperBound = 3000000 
        elif frequencyBands == "300 MHz - 3 GHz":
            lowerBound = 300000
            upperBound = 3000000
        elif frequencyBands == "3 - 30 GHz":
            lowerBound = 3000000
            upperBound = 30000000
        elif frequencyBands == "'30 - 300 GHz'":
            lowerBound = 30000000
            upperBound = 300000000

        if languageFromDataset == 'Bangla':
            lang = 'bn'
        elif languageFromDataset == 'English':
            lang = 'en'
        elif languageFromDataset == 'Koren':
            lang = 'ko'
        elif languageFromDataset == 'German':
            lang = 'de'
        elif languageFromDataset == 'Hebrew':
            lang = 'he'
        elif languageFromDataset == 'Hindi':
            lang = 'hi'
        elif languageFromDataset == 'Italian':
            lang = 'it'
        elif languageFromDataset == 'Japanese':
            lang = 'ja'
        elif languageFromDataset == 'Latin':
            lang = 'la'
        elif languageFromDataset == 'Malay':
            lang = 'ms'
        elif languageFromDataset == 'Nepali':
            lang = 'ne'
        elif languageFromDataset == 'Russian':
            lang = 'ru'
        elif languageFromDataset == 'Arabic':
            lang = 'ar'
        elif languageFromDataset == 'Chinese':
            lang = 'zh'
        elif languageFromDataset == 'Spanish':
            lang = 'es'
        
        if(state == "All"):
            dataset = df[(df['_lowerFrequency'] >= lowerBound) & (df['_lowerFrequency'] <= upperBound) 
                & (df['_status'] == searchType)]
        else:
            dataset = df[(df['_lowerFrequency'] >= lowerBound) & (df['_lowerFrequency'] <= upperBound) 
                & (df['_term'] == state) & (df['_status'] == searchType)]
    
        if(len(dataset) == 0):
            st.write("No data!")
        else:
            dataset['_term'] = dataset['_term'].apply(translator.translate, dest=lang).apply(getattr, args=('text',))
        
            colors = [
                "aqua",
                "aquamarine",
                "azure",
                "beige",
                "bisque",
                "blanchedalmond",
                "blue",
                "blueviolet",
                "brown",
                "burlywood",
                "cadetblue",
                "chartreuse",
                "chocolate",
                "coral",
                "cornflowerblue",
                "cornsilk",
                "crimson",
                "cyan",
                "darkblue",
                "darkcyan",
                "darkgoldenrod",
                "darkgray",
                "darkgreen",
                "darkkhaki",
                "darkmagenta",
                "darkolivegreen",
                "darkorange",
                "darkorchid",
                "darkred",
                "darksalmon",
                "darkseagreen",
                "darkslateblue",
                "darkslategray",
                "darkturquoise",
                "darkviolet",
                "deeppink",
                "deepskyblue",
                "dimgray",
                "dodgerblue",
                "firebrick",
                "floralwhite",
                "forestgreen",
                "fuchsia",
                "gainsboro",
                "ghostwhite",
                "gold",
                "goldenrod",
                "gray",
                "green",
                "greenyellow",
                "honeydew",
                "hotpink",
                "indianred",
                "indigo",
                "ivory",
                "khaki",
                "lavender",
                "lavenderblush",
                "lawngreen",
                "lemonchiffon",
                "lightblue",
                "lightcoral",
                "lightcyan",
                "lightgoldenrodyellow",
                "lightgreen",
                "lightgrey",
                "lightpink",
                "lightsalmon",
                "lightseagreen",
                "lightskyblue",
                "lightslategray",
                "lightsteelblue",
                "lightyellow",
                "lime",
                "limegreen",
                "linen",
                "magenta",
                "maroon",
                "mediumaquamarine",
                "mediumblue",
                "mediumorchid",
                "mediumpurple",
                "mediumseagreen",
                "mediumslateblue",
                "mediumspringgreen",
                "mediumturquoise",
                "mediumvioletred",
                "midnightblue",
                "mintcream",
                "mistyrose",
                "moccasin",
                "navajowhite",
                "navy",
                "navyblue",
                "oldlace",
                "olive",
                "olivedrab",
                "orange",
                "orangered",
                "orchid",
                "palegoldenrod",
                "palegreen",
                "paleturquoise",
                "palevioletred",
                "papayawhip",
                "peachpuff",
                "peru",
                "pink",
                "plum",
                "powderblue",
                "purple",
                "red",
                "rosybrown",
                "royalblue",
                "saddlebrown",
                "salmon",
                "sandybrown",
                "seagreen",
                "seashell",
                "sienna",
                "silver",
                "skyblue",
                "slateblue",
                "slategray",
                "snow",
                "springgreen",
                "steelblue",
                "tan",
                "teal",
                "thistle",
                "tomato",
                "turquoise",
                "violet",
                "wheat",
                "white",
                "whitesmoke",
                "yellow",
                "yellowgreen",
            ]

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

            for i in range(len(df2)):
                html_string.append(
                    f"""
                <div style="background-color:{colors[i]};">
                    <h5>{df2["_term"].loc[i]}</h5>
                    <p>{df2["_lowerFrequency"].loc[i]} - {df2["_higherFrequency"].loc[i]}</p>
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

   #st.image("https://static.streamlit.io/examples/owl.jpg", width=200)