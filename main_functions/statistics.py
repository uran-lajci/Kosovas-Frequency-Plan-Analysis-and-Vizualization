from main_functions.slider_utils import *
from main_functions.filter_utils import *
from main_functions.convert_values import *

import streamlit as st
import plotly.express as px
import re

def statistics(dataset):
    with st.form(key='statistics'):
        st.subheader("Search if a specific frequency is free!")
        col1, col2 = st.columns(2)
        with col1:
            number = st.number_input('Insert a number')
        with col2:
            frequency_unit = st.selectbox('Frequency Units', (
                'KHz',
                'MHz',
                'GHz',
            ))

        submit_search = st.form_submit_button(label='Search')

        free_frequency = []
        if submit_search:
            if frequency_unit == 'KHz':
                free_frequency = dataset[(dataset["_lowerFrequency"] <= number * 1000) & (dataset["_higherFrequency"] >= number * 1000)]
            elif frequency_unit == 'MHz':
                free_frequency = dataset[(dataset["_lowerFrequency"] <= number * 1000000) & (dataset["_higherFrequency"] >= number * 1000000)]
            elif frequency_unit == 'GHz':
                free_frequency = dataset[(dataset["_lowerFrequency"] <= number * 1000000000) & (dataset["_higherFrequency"] >= number * 1000000)]

            if len(free_frequency) > 0:
                st.write("There are ", len(free_frequency), " rows in this frequency")
                dataset_with_reseted_indexes = free_frequency.reset_index(drop=True)
                new_rows_lower = []
                for i in range(len(dataset_with_reseted_indexes["_lowerFrequency"])):
                    new_rows_lower.append(convertValuesAsString(dataset_with_reseted_indexes["_lowerFrequency"].loc[i]))

                new_rows_higher = []
                for i in range(len(dataset_with_reseted_indexes["_higherFrequency"])):
                    new_rows_higher.append(convertValuesAsString(dataset_with_reseted_indexes["_higherFrequency"].loc[i]))

                dataset_with_reseted_indexes["_lowerFrequency"] = new_rows_lower
                dataset_with_reseted_indexes["_higherFrequency"] = new_rows_higher

                st.write(dataset_with_reseted_indexes.drop(['_shortComments'], axis=1))
            else:
                st.write("This frequency is free")

    with st.form(key='statistics_groupByTerm'):
        st.subheader("Group by Frequency Service")
        term = dataset['service'].unique()
        frequency_term = st.selectbox('Frequency Service', term)
        submit_search = st.form_submit_button(label='Search')

        if submit_search:
            group_by_term = dataset[(dataset["service"] == frequency_term)]
            tabTable, tabPlot = st.tabs(["table", "plot"])

            with tabTable:
                dataset_with_reseted_indexes = group_by_term.reset_index(drop=True)
                new_rows_lower = []
                for i in range(len(dataset_with_reseted_indexes["_lowerFrequency"])):
                    new_rows_lower.append(convertValuesAsString(dataset_with_reseted_indexes["_lowerFrequency"].loc[i]))

                new_rows_higher = []
                for i in range(len(dataset_with_reseted_indexes["_higherFrequency"])):
                    new_rows_higher.append(convertValuesAsString(dataset_with_reseted_indexes["_higherFrequency"].loc[i]))

                dataset_with_reseted_indexes["_lowerFrequency"] = new_rows_lower
                dataset_with_reseted_indexes["_higherFrequency"] = new_rows_higher

                st.table(dataset_with_reseted_indexes.drop(['_shortComments'], axis=1))

            with tabPlot:
                rowes_in_MHz = {}
                rowes_in_MHz['_lowerFrequency'] = group_by_term['_lowerFrequency'] / 10 ** 6
                rowes_in_MHz['_higherFrequency'] = group_by_term['_higherFrequency'] / 10 ** 6
                rowes_in_MHz['_status'] = group_by_term["_status"]
                fig = px.scatter(
                    rowes_in_MHz,
                    x="_lowerFrequency",
                    y="_status",
                    size="_lowerFrequency",
                    color="_lowerFrequency",
                    hover_name="_status",
                    log_x=True,
                    size_max=60,
                )
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with st.form(key='statistics_groupByStatus'):
        st.subheader("Group by Frequency Status")        
        status = dataset['_status'].unique()
        frequency_status = st.selectbox('Frequency Status', (status))
        submit_search = st.form_submit_button(label='Search')

        if submit_search:
            group_by_status = dataset[(dataset["_status"] == frequency_status)]
            tabTable, tabPlot = st.tabs(["table", "plot"])

            with tabTable:
                dataset_with_reseted_indexes = group_by_status.reset_index(drop=True)
                new_rows_lower = []
                for i in range(len(dataset_with_reseted_indexes["_lowerFrequency"])):
                    new_rows_lower.append(convertValuesAsString(dataset_with_reseted_indexes["_lowerFrequency"].loc[i]))
                new_rows_higher = []
                for i in range(len(dataset_with_reseted_indexes["_higherFrequency"])):
                    new_rows_higher.append(convertValuesAsString(dataset_with_reseted_indexes["_higherFrequency"].loc[i]))

                dataset_with_reseted_indexes["_lowerFrequency"] = new_rows_lower
                dataset_with_reseted_indexes["_higherFrequency"] = new_rows_higher

                st.table(dataset_with_reseted_indexes.drop(['_shortComments'], axis=1))

            with tabPlot:
                rowes_in_MHz = {}
                rowes_in_MHz['_lowerFrequency'] = group_by_status['_lowerFrequency'] / 10 ** 6
                rowes_in_MHz['_higherFrequency'] = group_by_status['_higherFrequency'] / 10 ** 6
                rowes_in_MHz['service'] = group_by_status["service"]
                fig = px.scatter(
                    rowes_in_MHz,
                    x="_lowerFrequency",
                    y="service",
                    size="_lowerFrequency",
                    color="service",
                    hover_name="_higherFrequency",
                    log_x=True,
                    size_max=60,)
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)

def check_word_in_file(file_path, word):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        if re.search(word, file_contents):
            return True
    return False

def getStatistics(df):
    st.header("Statistics for experts")

    login, signup = st.tabs(["Login", "Signup"])

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
            statistics(df)
        else:
            st.error("Invalid username or password.")

    with signup:
        st.title("Signup Form")
        username = st.text_input("Username", key="rusername")
        password = st.text_input("Password", type="password", key="rpassword")
        password_confirm = st.text_input("Confirm Password", type="password", key="password_confirm")
        
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
