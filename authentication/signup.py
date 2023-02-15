from utils.general_utils import *

import streamlit as st

def getSignup():
    st.title("Signup Form")
    username = st.text_input("Username", key="rusername")
    password = st.text_input("Password", type="password", key="rpassword")
    password_confirm = st.text_input("Confirm Password", type="password", key="password_confirm")
    
    if not all([username,password,password_confirm]):
        st.error("All fields are required.")
    elif password != password_confirm:
        st.error("Passwords do not match.")
    else:
        file_path = 'authentication/usernames_and_passwords.txt'

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