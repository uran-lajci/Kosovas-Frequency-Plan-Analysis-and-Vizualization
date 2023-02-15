from utils.general_utils import *

import streamlit as st
import hashlib

def isLogedIn():
    login_successful = False
    st.title("Login Form")

    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")

    if not all([username,password]):
        st.error("Username and password are required fields.")
    else:
        file_path = 'authentication/usernames_and_passwords.txt'
        hashed_password = hashlib.sha256(("salt" + password).encode()).hexdigest()

        if check_word_in_file(file_path, username + ", Password:") and check_word_in_file(file_path, ": " + hashed_password):
            login_successful = True
        else:
            login_successful = False

    if login_successful:
        st.success("Welcome, {}!".format(username))
        return True
    else:
        st.error("Invalid username or password.")
        return False